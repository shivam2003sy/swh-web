/**
 * Copyright (C) 2018  The Software Heritage developers
 * See the AUTHORS file at the top-level directory of this distribution
 * License: GNU Affero General Public License version 3, or any later version
 * See top-level LICENSE file for more information
 */

import {handleFetchError, csrfPost, isGitRepoUrl} from 'utils/functions';
import {validate} from 'validate.js';

let saveRequestsTable;

export function initOriginSave() {

  $(document).ready(() => {

    fetch(Urls.browse_origin_save_types_list())
      .then(response => response.json())
      .then(data => {
        for (let originType of data) {
          $('#swh-input-origin-type').append(`<option value="${originType}">${originType}</option>`);
        }
      });

    saveRequestsTable = $('#swh-origin-save-requests').DataTable({
      serverSide: true,
      ajax: Urls.browse_origin_save_requests_list('all'),
      columns: [
        {
          data: 'save_request_date',
          name: 'request_date',
          render: (data, type, row) => {
            if (type === 'display') {
              let date = new Date(data);
              return date.toLocaleString();
            }
            return data;
          }
        },
        {
          data: 'origin_type',
          name: 'origin_type'

        },
        {
          data: 'origin_url',
          name: 'origin_url',
          render: (data, type, row) => {
            if (type === 'display') {
              return `<a href="${data}">${data}</a>`;
            }
            return data;
          }
        },
        {
          data: 'save_request_status',
          name: 'status'
        },
        {
          data: 'save_task_status',
          name: 'save_task_status',
          render: (data, type, row) => {
            if (data === 'succeed') {
              let browseOriginUrl = Urls.browse_origin(row.origin_url);
              if (row.visit_date) {
                browseOriginUrl += `visit/${row.visit_date}/`;
              }
              return `<a href="${browseOriginUrl}">${data}</a>`;
            }
            return data;
          }
        }
      ],
      scrollY: '50vh',
      scrollCollapse: true,
      order: [[0, 'desc']]
    });

    setInterval(() => {
      saveRequestsTable.ajax.reload(null, false);
    }, 5000);

    $('#swh-origin-save-requests-list-tab').on('shown.bs.tab', () => {
      saveRequestsTable.draw();
    });

    $('#swh-save-origin-form').submit(event => {
      event.preventDefault();
      event.stopPropagation();
      if (event.target.checkValidity()) {
        $(event.target).removeClass('was-validated');
        let originType = $('#swh-input-origin-type').val();
        let originUrl = $('#swh-input-origin-url').val();
        let addSaveOriginRequestUrl = Urls.browse_origin_save_request(originType, originUrl);
        let grecaptchaData = {'g-recaptcha-response': grecaptcha.getResponse()};
        let headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        };
        let body = JSON.stringify(grecaptchaData);
        csrfPost(addSaveOriginRequestUrl, headers, body)
          .then(handleFetchError)
          .then(response => response.json())
          .then(data => {
            if (data.save_request_status === 'accepted') {
              $('#swh-origin-save-request-status').css('color', 'green');
              $('#swh-origin-save-request-status').text(
                'The "save code now" request has been accepted and will be processed as soon as possible.');
            } else {
              $('#swh-origin-save-request-status').css('color', '#fecd1b');
              $('#swh-origin-save-request-status').text(
                'The "save code now" request has been put in pending state and may be accepted for processing after manual review.');
            }
            grecaptcha.reset();
          })
          .catch(response => {
            if (response.status === 403) {
              $('#swh-origin-save-request-status').css('color', 'red');
              $('#swh-origin-save-request-status').text(
                'The "save code now" request has been rejected because the reCAPTCHA could not be validated or the provided origin url is blacklisted.');
            }
            grecaptcha.reset();
          });
      } else {
        $(event.target).addClass('was-validated');
      }
    });

    $('#swh-show-origin-save-requests-list').on('click', (event) => {
      event.preventDefault();
      $('.nav-tabs a[href="#swh-origin-save-requests-list"]').tab('show');
    });

    $('#swh-input-origin-url').on('input', function(event) {
      let originUrl = $(this).val();
      $('#swh-input-origin-type option').each(function() {
        let val = $(this).val();
        if (val && originUrl.includes(val)) {
          $(this).prop('selected', true);
        }
      });
    });

  });

}

export function validateSaveOriginUrl(input) {
  let validUrl = validate({website: input.value}, {
    website: {
      url: {
        schemes: ['http', 'https', 'svn', 'git']
      }
    }
  }) === undefined;
  let originType = $('#swh-input-origin-type').val();
  if (originType === 'git' && validUrl) {
    // additional checks for well known code hosting providers
    let githubIdx = input.value.indexOf('://github.com');
    let gitlabIdx = input.value.indexOf('://gitlab.com');
    let gitSfIdx = input.value.indexOf('://git.code.sf.net');
    let bitbucketIdx = input.value.indexOf('://bitbucket.org');
    if (githubIdx !== -1 && githubIdx <= 5) {
      validUrl = isGitRepoUrl(input.value, 'github.com');
    } else if (gitlabIdx !== -1 && gitlabIdx <= 5) {
      validUrl = isGitRepoUrl(input.value, 'gitlab.com');
    } else if (gitSfIdx !== -1 && gitSfIdx <= 5) {
      validUrl = isGitRepoUrl(input.value, 'git.code.sf.net/p');
    } else if (bitbucketIdx !== -1 && bitbucketIdx <= 5) {
      validUrl = isGitRepoUrl(input.value, 'bitbucket.org');
    }
  }
  if (validUrl) {
    input.setCustomValidity('');
  } else {
    input.setCustomValidity('The origin url is not valid or does not reference a code repository');
  }
}
