!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports?exports.admin=t():(e.swh=e.swh||{},e.swh.admin=t())}(window,(function(){return function(e){var t={};function n(r){if(t[r])return t[r].exports;var a=t[r]={i:r,l:!1,exports:{}};return e[r].call(a.exports,a,a.exports,n),a.l=!0,a.exports}return n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)n.d(r,a,function(t){return e[t]}.bind(null,a));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/static/",n(n.s=240)}({155:function(e,t,n){"use strict";function r(e){var t=0;if("undefined"==typeof Symbol||null==e[Symbol.iterator]){if(Array.isArray(e)||(e=function(e,t){if(!e)return;if("string"==typeof e)return a(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return a(e,t)}(e)))return function(){return t>=e.length?{done:!0}:{done:!1,value:e[t++]}};throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}return(t=e[Symbol.iterator]()).next.bind(t)}function a(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function i(e,t){if("display"===t&&(e&&e.startsWith("swh")))return'<a href="'+Urls.browse_swh_id(e)+'">'+e+"</a>";return e}function s(e,t){if(""===t)return!1;for(var n in e){var r=e[n];if(("string"==typeof r||r instanceof String)&&-1!==r.search(t))return!0}return!1}function o(){var e;$(document).ready((function(){$.fn.dataTable.ext.errMode="none",e=$("#swh-admin-deposit-list").on("error.dt",(function(e,t,n,r){$("#swh-admin-deposit-list-error").text(r)})).DataTable({serverSide:!0,processing:!0,dom:'<<f<"#list-exclude">l>rt<"bottom"ip>>',ajax:{url:Urls.admin_deposit_list(),dataFilter:function(e){for(var t,n=jQuery.parseJSON(e),a=$("#swh-admin-deposit-list-exclude-filter").val(),i=0,o=[],u=r(n.data);!(t=u()).done;){var d=t.value;s(d,a)?i+=1:o.push(d)}return n.recordsFiltered=i,n.data=o,JSON.stringify(n)}},columns:[{data:"id",name:"id"},{data:"swh_id_context",name:"swh_id_context",render:function(e,t,n){if(e&&"display"===t){var r=e.indexOf(";origin=");if(-1!==r){var a=e.slice(r+";origin=".length),i=a.indexOf(";");return-1!==i&&(a=a.slice(0,i)),'<a href="'+a+'">'+a+"</a>"}}return e}},{data:"reception_date",name:"reception_date",render:function(e,t,n){return"display"===t?new Date(e).toLocaleString():e}},{data:"status",name:"status"},{data:"status_detail",name:"status_detail",render:function(e,t,n){if("display"===t&&e){var r=e;return"object"==typeof e&&(r=JSON.stringify(e,null,4)),'<div style="width: 200px; white-space: pre; overflow-x: auto;">'+r+"</div>"}return e},orderable:!1,visible:!1},{data:"swh_id",name:"swh_id",render:function(e,t,n){return i(e,t)},orderable:!1,visible:!1},{data:"swh_id_context",name:"swh_id_context",render:function(e,t,n){return i(e,t)},orderable:!1,visible:!1}],scrollX:!0,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]]}),$("div#list-exclude").html('<div id="swh-admin-deposit-list-exclude-wrapper">\n    <div id="swh-admin-deposit-list-exclude-div-wrapper" class="dataTables_filter">\n      <label>\n        Exclude:<input id="swh-admin-deposit-list-exclude-filter"\n                       type="search"\n                       value="check-deposit"\n                       class="form-control form-control-sm"\n                       placeholder="exclude-pattern" aria-controls="swh-admin-deposit-list">\n          </input>\n      </label>\n    </div>\n  </div>\n'),$("#swh-admin-deposit-list-exclude-filter").keyup((function(){e.draw()})),e.draw()})),$("a.toggle-col").on("click",(function(t){t.preventDefault();var n=e.column($(this).attr("data-column"));n.visible(!n.visible()),n.visible()?$(this).removeClass("col-hidden"):$(this).addClass("col-hidden")}))}n.d(t,"a",(function(){return o}))},156:function(e,t,n){"use strict";n.d(t,"e",(function(){return c})),n.d(t,"b",(function(){return f})),n.d(t,"h",(function(){return h})),n.d(t,"c",(function(){return p})),n.d(t,"k",(function(){return v})),n.d(t,"a",(function(){return g})),n.d(t,"f",(function(){return w})),n.d(t,"i",(function(){return b})),n.d(t,"g",(function(){return _})),n.d(t,"j",(function(){return y})),n.d(t,"d",(function(){return x}));var r,a,i,s,o,u=n(2),d=n(21);function l(e){$(e+" tbody").on("click","tr",(function(){$(this).hasClass("selected")?($(this).removeClass("selected"),$(e).closest(".tab-pane").find(".swh-action-need-selection").prop("disabled",!0)):($(e+" tr.selected").removeClass("selected"),$(this).addClass("selected"),$(e).closest(".tab-pane").find(".swh-action-need-selection").prop("disabled",!1))}))}function c(){$(document).ready((function(){$.fn.dataTable.ext.errMode="throw",r=$("#swh-authorized-origin-urls").DataTable({serverSide:!0,ajax:Urls.admin_origin_save_authorized_urls_list(),columns:[{data:"url",name:"url"}],scrollY:"50vh",scrollCollapse:!0,info:!1}),l("#swh-authorized-origin-urls"),swh.webapp.addJumpToPagePopoverToDataTable(r),a=$("#swh-unauthorized-origin-urls").DataTable({serverSide:!0,ajax:Urls.admin_origin_save_unauthorized_urls_list(),columns:[{data:"url",name:"url"}],scrollY:"50vh",scrollCollapse:!0,info:!1}),l("#swh-unauthorized-origin-urls"),swh.webapp.addJumpToPagePopoverToDataTable(a);var e=[{data:"id",name:"id",visible:!1,searchable:!1},{data:"save_request_date",name:"request_date",render:function(e,t,n){return"display"===t?new Date(e).toLocaleString():e}},{data:"visit_type",name:"visit_type"},{data:"origin_url",name:"origin_url",render:function(e,t,n){if("display"===t){var r="",a=$.fn.dataTable.render.text().display(e);if("succeed"===n.save_task_status){var i=Urls.browse_origin()+"?origin_url="+a;r+='<a href="'+(i+="&amp;timestamp="+n.visit_date)+'">'+a+"</a>"}else r+=a;return r+='&nbsp;<a href="'+a+'"><i class="mdi mdi-open-in-new" aria-hidden="true"></i></a>'}return e}}];i=$("#swh-origin-save-pending-requests").DataTable({serverSide:!0,processing:!0,language:{processing:'<img src="'+d.c+'"></img>'},ajax:Urls.origin_save_requests_list("pending"),searchDelay:1e3,columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]],responsive:{details:{type:"none"}}}),l("#swh-origin-save-pending-requests"),swh.webapp.addJumpToPagePopoverToDataTable(i),o=$("#swh-origin-save-rejected-requests").DataTable({serverSide:!0,processing:!0,language:{processing:'<img src="'+d.c+'"></img>'},ajax:Urls.origin_save_requests_list("rejected"),searchDelay:1e3,columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]],responsive:{details:{type:"none"}}}),l("#swh-origin-save-rejected-requests"),swh.webapp.addJumpToPagePopoverToDataTable(o),e.push({data:"save_task_status",name:"save_task_status"}),e.push({name:"info",render:function(e,t,n){return"succeed"===n.save_task_status||"failed"===n.save_task_status?'<i class="mdi mdi-information-outline swh-save-request-info" aria-hidden="true" style="cursor: pointer"onclick="swh.admin.displaySaveRequestInfo(event, '+n.id+')"></i>':""}}),s=$("#swh-origin-save-accepted-requests").DataTable({serverSide:!0,processing:!0,language:{processing:'<img src="'+d.c+'"></img>'},ajax:Urls.origin_save_requests_list("accepted"),searchDelay:1e3,columns:e,scrollY:"50vh",scrollCollapse:!0,order:[[0,"desc"]],responsive:{details:{type:"none"}}}),l("#swh-origin-save-accepted-requests"),swh.webapp.addJumpToPagePopoverToDataTable(s),$("#swh-origin-save-requests-nav-item").on("shown.bs.tab",(function(){i.draw()})),$("#swh-origin-save-url-filters-nav-item").on("shown.bs.tab",(function(){r.draw()})),$("#swh-authorized-origins-tab").on("shown.bs.tab",(function(){r.draw()})),$("#swh-unauthorized-origins-tab").on("shown.bs.tab",(function(){a.draw()})),$("#swh-save-requests-pending-tab").on("shown.bs.tab",(function(){i.draw()})),$("#swh-save-requests-accepted-tab").on("shown.bs.tab",(function(){s.draw()})),$("#swh-save-requests-rejected-tab").on("shown.bs.tab",(function(){o.draw()})),$("#swh-save-requests-pending-tab").click((function(){i.ajax.reload(null,!1)})),$("#swh-save-requests-accepted-tab").click((function(){s.ajax.reload(null,!1)})),$("#swh-save-requests-rejected-tab").click((function(){o.ajax.reload(null,!1)})),$("body").on("click",(function(e){$(e.target).parents(".popover").length>0?event.stopPropagation():0===$(e.target).parents(".swh-save-request-info").length&&$(".swh-save-request-info").popover("dispose")}))}))}function f(){var e=$("#swh-authorized-url-prefix").val(),t=Urls.admin_origin_save_add_authorized_url(e);Object(u.a)(t).then(u.b).then((function(){r.row.add({url:e}).draw(),$(".swh-add-authorized-origin-status").html(Object(u.d)("success","The origin url prefix has been successfully added in the authorized list.",!0))})).catch((function(e){$(".swh-add-authorized-origin-status").html(Object(u.d)("warning","The provided origin url prefix is already registered in the authorized list.",!0))}))}function h(){var e=$("#swh-authorized-origin-urls tr.selected").text();if(e){var t=Urls.admin_origin_save_remove_authorized_url(e);Object(u.a)(t).then(u.b).then((function(){r.row(".selected").remove().draw()})).catch((function(){}))}}function p(){var e=$("#swh-unauthorized-url-prefix").val(),t=Urls.admin_origin_save_add_unauthorized_url(e);Object(u.a)(t).then(u.b).then((function(){a.row.add({url:e}).draw(),$(".swh-add-unauthorized-origin-status").html(Object(u.d)("success","The origin url prefix has been successfully added in the unauthorized list.",!0))})).catch((function(){$(".swh-add-unauthorized-origin-status").html(Object(u.d)("warning","The provided origin url prefix is already registered in the unauthorized list.",!0))}))}function v(){var e=$("#swh-unauthorized-origin-urls tr.selected").text();if(e){var t=Urls.admin_origin_save_remove_unauthorized_url(e);Object(u.a)(t).then(u.b).then((function(){a.row(".selected").remove().draw()})).catch((function(){}))}}function g(){var e=i.row(".selected");if(e.length){swh.webapp.showModalConfirm("Accept origin save request ?","Are you sure to accept this origin save request ?",(function(){var t=e.data(),n=Urls.admin_origin_save_request_accept(t.visit_type,t.origin_url);Object(u.a)(n).then((function(){i.ajax.reload(null,!1)}))}))}}function w(){var e=i.row(".selected");if(e.length){swh.webapp.showModalConfirm("Reject origin save request ?","Are you sure to reject this origin save request ?",(function(){var t=e.data(),n=Urls.admin_origin_save_request_reject(t.visit_type,t.origin_url);Object(u.a)(n).then((function(){i.ajax.reload(null,!1)}))}))}}function m(e){var t=e.row(".selected");if(t.length){var n=t.data().id;swh.webapp.showModalConfirm("Remove origin save request ?","Are you sure to remove this origin save request ?",(function(){var t=Urls.admin_origin_save_request_remove(n);Object(u.a)(t).then((function(){e.ajax.reload(null,!1)}))}))}}function b(){m(i)}function _(){m(s)}function y(){m(o)}function x(e,t){e.stopPropagation();var n=Urls.admin_origin_save_task_info(t);$(".swh-save-request-info").popover("dispose"),$(e.target).popover({title:"Save request task information",content:'<div class="swh-popover">\n                  <div class="text-center">\n                    <img src='+d.c+"></img>\n                    <p>Fetching task information ...</p>\n                  </div>\n                </div>",html:!0,placement:"left",sanitizeFn:swh.webapp.filterXSS}),$(e.target).popover("show"),fetch(n).then((function(e){return e.json()})).then((function(t){var n;if($.isEmptyObject(t))n="Not available";else{var r=[];r.push({key:"Task type",value:t.type}),t.hasOwnProperty("task_name")&&r.push({key:"Task name",value:t.name}),r.push({key:"Task arguments",value:JSON.stringify(t.arguments,null,2)}),r.push({key:"Task id",value:t.id}),r.push({key:"Task backend id",value:t.backend_id}),r.push({key:"Task scheduling date",value:new Date(t.scheduled).toLocaleString()}),r.push({key:"Task termination date",value:new Date(t.ended).toLocaleString()}),t.hasOwnProperty("duration")&&r.push({key:"Task duration",value:t.duration+" s"}),t.hasOwnProperty("worker")&&r.push({key:"Task executor",value:t.worker}),t.hasOwnProperty("message")&&r.push({key:"Task log",value:t.message}),n='<table class="table"><tbody>';for(var a=0,i=r;a<i.length;a++){var s=i[a];n+='<tr>\n              <th class="swh-metadata-table-row swh-metadata-table-key">'+s.key+'</th>\n              <td class="swh-metadata-table-row swh-metadata-table-value">\n                <pre>'+s.value+"</pre>\n              </td>\n            </tr>"}n+="</tbody></table>"}$(".swh-popover").html(n),$(e.target).popover("update")}))}},2:function(e,t,n){"use strict";function r(e){if(!e.ok)throw e;return e}function a(e){for(var t=0;t<e.length;++t)if(!e[t].ok)throw e[t];return e}function i(e){return"/static/"+e}function s(e,t,n){return void 0===t&&(t={}),void 0===n&&(n=null),t["X-CSRFToken"]=Cookies.get("csrftoken"),fetch(e,{credentials:"include",headers:t,method:"POST",body:n})}function o(e,t){return new RegExp("(?:git|https?|git@)(?:\\:\\/\\/)?"+t+"[/|:][A-Za-z0-9-/]+?\\/[\\w\\.-]+\\/?(?!=.git)(?:\\.git(?:\\/?|\\#[\\w\\.\\-_]+)?)?$").test(e)}function u(){history.replaceState("",document.title,window.location.pathname+window.location.search)}function d(e,t){var n=window.getSelection();n.removeAllRanges();var r=document.createRange();r.setStart(e,0),"#text"!==t.nodeName?r.setEnd(t,t.childNodes.length):r.setEnd(t,t.textContent.length),n.addRange(r)}function l(e,t,n){void 0===n&&(n=!1);var r="",a="";return n&&(r='<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n        <span aria-hidden="true">&times;</span>\n      </button>',a="alert-dismissible"),'<div class="alert alert-'+e+" "+a+'" role="alert">'+t+r+"</div>"}n.d(t,"b",(function(){return r})),n.d(t,"c",(function(){return a})),n.d(t,"h",(function(){return i})),n.d(t,"a",(function(){return s})),n.d(t,"e",(function(){return o})),n.d(t,"f",(function(){return u})),n.d(t,"g",(function(){return d})),n.d(t,"d",(function(){return l}))},21:function(e,t,n){"use strict";n.d(t,"b",(function(){return a})),n.d(t,"a",(function(){return i})),n.d(t,"c",(function(){return s}));var r=n(2),a=768,i=992,s=Object(r.h)("img/swh-spinner.gif")},240:function(e,t,n){e.exports=n(241)},241:function(e,t,n){"use strict";n.r(t);var r=n(155);n.d(t,"initDepositAdmin",(function(){return r.a}));var a=n(156);n.d(t,"initOriginSaveAdmin",(function(){return a.e})),n.d(t,"addAuthorizedOriginUrl",(function(){return a.b})),n.d(t,"removeAuthorizedOriginUrl",(function(){return a.h})),n.d(t,"addUnauthorizedOriginUrl",(function(){return a.c})),n.d(t,"removeUnauthorizedOriginUrl",(function(){return a.k})),n.d(t,"acceptOriginSaveRequest",(function(){return a.a})),n.d(t,"rejectOriginSaveRequest",(function(){return a.f})),n.d(t,"removePendingOriginSaveRequest",(function(){return a.i})),n.d(t,"removeAcceptedOriginSaveRequest",(function(){return a.g})),n.d(t,"removeRejectedOriginSaveRequest",(function(){return a.j})),n.d(t,"displaySaveRequestInfo",(function(){return a.d}))}})}));
//# sourceMappingURL=admin.77aa2162ca225ce7a697.js.map