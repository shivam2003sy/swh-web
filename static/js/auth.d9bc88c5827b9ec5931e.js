!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports?exports.swh=t():(e.swh=e.swh||{},e.swh.auth=t())}(self,(function(){return function(){"use strict";var e={45149:function(e,t,o){function n(e){if(!e.ok)throw e;return e}function r(e,t,o){return void 0===t&&(t={}),void 0===o&&(o=null),t["X-CSRFToken"]=Cookies.get("csrftoken"),fetch(e,{credentials:"include",headers:t,method:"POST",body:o})}function i(){history.replaceState("",document.title,window.location.pathname+window.location.search)}o.d(t,{ry:function(){return n},e_:function(){return r},L3:function(){return i}})}},t={};function o(n){var r=t[n];if(void 0!==r)return r.exports;var i=t[n]={exports:{}};return e[n](i,i.exports,o),i.exports}o.d=function(e,t){for(var n in t)o.o(t,n)&&!o.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})};var n={};return function(){o.r(n),o.d(n,{applyTokenAction:function(){return u},initProfilePage:function(){return f}});var e,t=o(45149);function r(e){return'<p id="swh-token-error-message" class="mt-3 swh-token-form-message">'+e+"</p>"}function i(){window.location=Urls.oidc_generate_bearer_token()}function a(e){var o={token_id:e};(0,t.e_)(Urls.oidc_get_bearer_token(),{},JSON.stringify(o)).then(t.ry).then((function(e){return e.text()})).then((function(e){var t='<p>Below is your token.</p>\n         <pre id="swh-bearer-token" class="mt-3">'+e+"</pre>";swh.webapp.showModalHtml("Display bearer token",t)})).catch((function(){swh.webapp.showModalHtml("Display bearer token",r("Internal server error."))}))}function s(o){var n={token_ids:o};(0,t.e_)(Urls.oidc_revoke_bearer_tokens(),{},JSON.stringify(n)).then(t.ry).then((function(){$("#swh-token-form-submit").prop("disabled",!0),$("#swh-token-form-message").html('<p id="swh-token-success-message" class="mt-3 swh-token-form-message">'+("Bearer token"+(o.length>1?"s":"")+" successfully revoked.")+"</p>"),e.draw()})).catch((function(){$("#swh-token-form-message").html(r("Internal server error."))}))}function l(e){s([e])}function c(){for(var t=[],o=e.rows().data(),n=0;n<o.length;++n)t.push(o[n].id);s(t)}function u(e,t){var o,n,r={display:{submitCallback:a},generate:{modalTitle:"Bearer token generation",infoText:"Click on the button to generate the token. You will be redirected to Software Heritage Authentication Service and might be asked to enter your password again.",buttonText:"Generate token",submitCallback:i},revoke:{modalTitle:"Revoke bearer token",infoText:"Click on the button to revoke the token.",buttonText:"Revoke token",submitCallback:l},revokeAll:{modalTitle:"Revoke all bearer tokens",infoText:"Click on the button to revoke all tokens.",buttonText:"Revoke tokens",submitCallback:c}};if(r[e])if("display"!==e){var s=(o=r[e].infoText,n=r[e].buttonText,'<form id="swh-token-form" class="text-center">\n      <p id="swh-token-form-text">'+o+'</p>\n      <input id="swh-token-form-submit" type="submit" value="'+n+'">\n      <div id="swh-token-form-message"></div>\n    </form>');swh.webapp.showModalHtml(r[e].modalTitle,s),$("#swh-token-form").submit((function(o){o.preventDefault(),o.stopPropagation(),r[e].submitCallback(t)}))}else r[e].submitCallback(t)}function f(){$(document).ready((function(){e=$("#swh-bearer-tokens-table").on("error.dt",(function(e,t,o,n){$("#swh-origin-save-request-list-error").text("An error occurred while retrieving the tokens list"),console.log(n)})).DataTable({serverSide:!0,ajax:Urls.oidc_list_bearer_tokens(),columns:[{data:"creation_date",name:"creation_date",render:function(e,t,o){return"display"===t?new Date(e).toLocaleString():e}},{render:function(e,t,o){return'<button class="btn btn-default"\n                         onclick="swh.auth.applyTokenAction(\'display\', '+o.id+')">\n                  Display token\n                </button>\n                <button class="btn btn-default"\n                        onclick="swh.auth.applyTokenAction(\'revoke\', '+o.id+')">\n                  Revoke token\n                </button>'}}],ordering:!1,searching:!1,scrollY:"50vh",scrollCollapse:!0}),$("#swh-oidc-profile-tokens-tab").on("shown.bs.tab",(function(){e.draw(),window.location.hash="#tokens"})),$("#swh-oidc-profile-account-tab").on("shown.bs.tab",(function(){(0,t.L3)()})),"#tokens"===window.location.hash&&$('.nav-tabs a[href="#swh-oidc-profile-tokens"]').tab("show")}))}}(),n}()}));
//# sourceMappingURL=auth.d9bc88c5827b9ec5931e.js.map