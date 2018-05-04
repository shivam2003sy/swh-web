/**
 * Copyright (C) 2018  The Software Heritage developers
 * See the AUTHORS file at the top-level directory of this distribution
 * License: GNU Affero General Public License version 3, or any later version
 * See top-level LICENSE file for more information
 */

export async function renderMarkdown(domElt, markdownDocUrl) {

  let showdown = await import(/* webpackChunkName: "showdown" */ 'utils/showdown');

  $(document).ready(() => {
    let converter = new showdown.Converter({tables: true});
    fetch(markdownDocUrl, {credentials: 'same-origin'})
      .then(response => response.text())
      .then(data => {
        $(domElt).html(converter.makeHtml(data));
      });
  });

}
