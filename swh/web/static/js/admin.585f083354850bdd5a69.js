!function(e,r){"object"==typeof exports&&"object"==typeof module?module.exports=r():"function"==typeof define&&define.amd?define([],r):"object"==typeof exports?exports.admin=r():(e.swh=e.swh||{},e.swh.admin=r())}(window,function(){return function(e){var r={};function t(n){if(r[n])return r[n].exports;var i=r[n]={i:n,l:!1,exports:{}};return e[n].call(i.exports,i,i.exports,t),i.l=!0,i.exports}return t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:n})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,r){if(1&r&&(e=t(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(t.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var i in e)t.d(n,i,function(r){return e[r]}.bind(null,i));return n},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},t.p="/static/",t(t.s=214)}({214:function(e,r,t){e.exports=t(436)},3:function(e,r,t){"use strict";function n(e){if(!e.ok)throw e;return e}function i(e){for(var r=0;r<e.length;++r)if(!e[r].ok)throw e[r];return e}function a(e){return"/static/"+e}function o(e,r,t){return void 0===r&&(r={}),void 0===t&&(t=null),r["X-CSRFToken"]=Cookies.get("csrftoken"),fetch(e,{credentials:"include",headers:r,method:"POST",body:t})}function s(e,r){return new RegExp("(?:git|https?|git@)(?:\\:\\/\\/)?"+r+"[/|:][A-Za-z0-9-]+?\\/[\\w\\.-]+\\/?(?!=.git)(?:\\.git(?:\\/?|\\#[\\w\\.\\-_]+)?)?$").test(e)}function u(){history.replaceState("",document.title,window.location.pathname+window.location.search)}t.d(r,"b",function(){return n}),t.d(r,"c",function(){return i}),t.d(r,"f",function(){return a}),t.d(r,"a",function(){return o}),t.d(r,"d",function(){return s}),t.d(r,"e",function(){return u})},32:function(e,r,t){e.exports=t(73)},4:function(e,r){var t=e.exports={version:"2.5.7"};"number"==typeof __e&&(__e=t)},436:function(e,r,t){"use strict";t.r(r);var n=t(32),i=t.n(n);function a(){$(document).ready(function(){$.fn.dataTable.ext.errMode="none",$("#swh-admin-deposit-list").on("error.dt",function(e,r,t,n){$("#swh-admin-deposit-list-error").text(n)}).DataTable({serverSide:!0,ajax:Urls.admin_deposit_list(),columns:[{data:"id",name:"id"},{data:"external_id",name:"external_id",render:function(e,r,t){return"display"===r&&e&&e.startsWith("hal")?'<a href="https://hal.archives-ouvertes.fr/'+e+'">'+e+"</a>":e}},{data:"reception_date",name:"reception_date",render:function(e,r,t){return"display"===r?new Date(e).toLocaleString():e}},{data:"status",name:"status"},{data:"status_detail",name:"status_detail",render:function(e,r,t){if("display"===r&&e){var n=e;return"object"==typeof e&&(n=i()(e,null,4)),'<div style="width: 200px; white-space: pre; overflow-x: auto;">'+n+"</div>"}return e},orderable:!1},{data:"swh_id",name:"swh_id",render:function(e,r,t){if("display"===r&&(e&&e.startsWith("swh")))return'<a href="'+Urls.browse_swh_id(e)+'">'+e+"</a>";return e}}],scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]]}).draw()})}var o,s,u,d,l,c=t(3);function f(e){$(e+" tbody").on("click","tr",function(){$(this).hasClass("selected")?$(this).removeClass("selected"):($(e+" tr.selected").removeClass("selected"),$(this).addClass("selected"))})}function h(){$(document).ready(function(){$.fn.dataTable.ext.errMode="throw",o=$("#swh-authorized-origin-urls").DataTable({serverSide:!0,ajax:Urls.admin_origin_save_authorized_urls_list(),columns:[{data:"url",name:"url"}],scrollY:"50vh",scrollCollapse:!0,info:!1}),f("#swh-authorized-origin-urls"),s=$("#swh-unauthorized-origin-urls").DataTable({serverSide:!0,ajax:Urls.admin_origin_save_unauthorized_urls_list(),columns:[{data:"url",name:"url"}],scrollY:"50vh",scrollCollapse:!0,info:!1}),f("#swh-unauthorized-origin-urls");var e=[{data:"save_request_date",name:"request_date",render:function(e,r,t){return"display"===r?new Date(e).toLocaleString():e}},{data:"origin_type",name:"origin_type"},{data:"origin_url",name:"origin_url",render:function(e,r,t){return"display"===r?'<a href="'+e+'">'+e+"</a>":e}}];u=$("#swh-origin-save-pending-requests").DataTable({serverSide:!0,ajax:Urls.browse_origin_save_requests_list("pending"),columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]]}),f("#swh-origin-save-pending-requests"),l=$("#swh-origin-save-rejected-requests").DataTable({serverSide:!0,ajax:Urls.browse_origin_save_requests_list("rejected"),columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]]}),e.push({data:"save_task_status",name:"save_task_status",render:function(e,r,t){return"succeed"===e?'<a href="'+Urls.browse_origin(t.origin_url)+'">'+e+"</a>":e}}),d=$("#swh-origin-save-accepted-requests").DataTable({serverSide:!0,ajax:Urls.browse_origin_save_requests_list("accepted"),columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]]}),$("#swh-origin-save-requests-nav-item").on("shown.bs.tab",function(){u.draw()}),$("#swh-origin-save-url-filters-nav-item").on("shown.bs.tab",function(){o.draw()}),$("#swh-authorized-origins-tab").on("shown.bs.tab",function(){o.draw()}),$("#swh-unauthorized-origins-tab").on("shown.bs.tab",function(){s.draw()}),$("#swh-save-requests-pending-tab").on("shown.bs.tab",function(){u.draw()}),$("#swh-save-requests-accepted-tab").on("shown.bs.tab",function(){d.draw()}),$("#swh-save-requests-rejected-tab").on("shown.bs.tab",function(){l.draw()}),$("#swh-save-requests-pending-tab").click(function(){u.ajax.reload(null,!1)}),$("#swh-save-requests-accepted-tab").click(function(){d.ajax.reload(null,!1)}),$("#swh-save-requests-rejected-tab").click(function(){l.ajax.reload(null,!1)})})}function p(){var e=$("#swh-authorized-url-prefix").val(),r=Urls.admin_origin_save_add_authorized_url(e);Object(c.a)(r).then(c.b).then(function(){o.row.add({url:e}).draw()}).catch(function(e){swh.webapp.showModalMessage("Duplicated origin url prefix","The provided origin url prefix is already registered in the authorized list.")})}function v(){var e=$("#swh-authorized-origin-urls tr.selected").text();if(e){var r=Urls.admin_origin_save_remove_authorized_url(e);Object(c.a)(r).then(c.b).then(function(){o.row(".selected").remove().draw()}).catch(function(){})}}function w(){var e=$("#swh-unauthorized-url-prefix").val(),r=Urls.admin_origin_save_add_unauthorized_url(e);Object(c.a)(r).then(c.b).then(function(){s.row.add({url:e}).draw()}).catch(function(){swh.webapp.showModalMessage("Duplicated origin url prefix","The provided origin url prefix is already registered in the unauthorized list.")})}function _(){var e=$("#swh-unauthorized-origin-urls tr.selected").text();if(e){var r=Urls.admin_origin_save_remove_unauthorized_url(e);Object(c.a)(r).then(c.b).then(function(){s.row(".selected").remove().draw()}).catch(function(){})}}function g(){var e=u.row(".selected");if(e.length){swh.webapp.showModalConfirm("Accept origin save request ?","Are you sure to accept this origin save request ?",function(){var r=e.data(),t=Urls.admin_origin_save_request_accept(r.origin_type,r.origin_url);Object(c.a)(t).then(function(){u.ajax.reload(null,!1)})})}}function b(){var e=u.row(".selected");if(e.length){swh.webapp.showModalConfirm("Reject origin save request ?","Are you sure to reject this origin save request ?",function(){var r=e.data(),t=Urls.admin_origin_save_request_reject(r.origin_type,r.origin_url);Object(c.a)(t).then(function(){u.ajax.reload(null,!1)})})}}t.d(r,"initDepositAdmin",function(){return a}),t.d(r,"initOriginSaveAdmin",function(){return h}),t.d(r,"addAuthorizedOriginUrl",function(){return p}),t.d(r,"removeAuthorizedOriginUrl",function(){return v}),t.d(r,"addUnauthorizedOriginUrl",function(){return w}),t.d(r,"removeUnauthorizedOriginUrl",function(){return _}),t.d(r,"acceptOriginSaveRequest",function(){return g}),t.d(r,"rejectOriginSaveRequest",function(){return b})},73:function(e,r,t){var n=t(4),i=n.JSON||(n.JSON={stringify:JSON.stringify});e.exports=function(e){return i.stringify.apply(i,arguments)}}})});
//# admin.585f083354850bdd5a69.js.map