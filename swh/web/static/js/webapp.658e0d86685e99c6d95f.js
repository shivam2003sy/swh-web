!function(t,n){"object"==typeof exports&&"object"==typeof module?module.exports=n():"function"==typeof define&&define.amd?define([],n):"object"==typeof exports?exports.webapp=n():(t.swh=t.swh||{},t.swh.webapp=n())}(window,function(){return function(t){function n(n){for(var r,o,s=n[0],u=n[1],a=n[2],f=0,p=[];f<s.length;f++)o=s[f],i[o]&&p.push(i[o][0]),i[o]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(t[r]=u[r]);for(l&&l(n);p.length;)p.shift()();return c.push.apply(c,a||[]),e()}function e(){for(var t,n=0;n<c.length;n++){for(var e=c[n],r=!0,o=1;o<e.length;o++){var u=e[o];0!==i[u]&&(r=!1)}r&&(c.splice(n--,1),t=s(s.s=e[0]))}return t}var r={},o={10:0},i={10:0},c=[];function s(n){if(r[n])return r[n].exports;var e=r[n]={i:n,l:!1,exports:{}};return t[n].call(e.exports,e,e.exports,s),e.l=!0,e.exports}s.e=function(t){var n=[];o[t]?n.push(o[t]):0!==o[t]&&{3:1,4:1,8:1}[t]&&n.push(o[t]=new Promise(function(n,e){for(var r="css/"+({3:"highlightjs",4:"org",6:"pdfjs",8:"showdown"}[t]||t)+"."+{3:"a60eec104cf7eb12dc0c",4:"a471382ee6892d357175",6:"ef2a116084ff15ae835f",8:"7a12c76fe3bdb24cc44a"}[t]+".css",i=s.p+r,c=document.getElementsByTagName("link"),u=0;u<c.length;u++){var a=(l=c[u]).getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(a===r||a===i))return n()}var f=document.getElementsByTagName("style");for(u=0;u<f.length;u++){var l;if((a=(l=f[u]).getAttribute("data-href"))===r||a===i)return n()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=n,p.onerror=function(n){var r=n&&n.target&&n.target.src||i,c=new Error("Loading CSS chunk "+t+" failed.\n("+r+")");c.request=r,delete o[t],p.parentNode.removeChild(p),e(c)},p.href=i,document.getElementsByTagName("head")[0].appendChild(p)}).then(function(){o[t]=0}));var e=i[t];if(0!==e)if(e)n.push(e[2]);else{var r=new Promise(function(n,r){e=i[t]=[n,r]});n.push(e[2]=r);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,s.nc&&u.setAttribute("nonce",s.nc),u.src=function(t){return s.p+"js/"+({3:"highlightjs",4:"org",6:"pdfjs",8:"showdown"}[t]||t)+"."+{3:"a60eec104cf7eb12dc0c",4:"a471382ee6892d357175",6:"ef2a116084ff15ae835f",8:"7a12c76fe3bdb24cc44a"}[t]+".js"}(t),c=function(n){u.onerror=u.onload=null,clearTimeout(a);var e=i[t];if(0!==e){if(e){var r=n&&("load"===n.type?"missing":n.type),o=n&&n.target&&n.target.src,c=new Error("Loading chunk "+t+" failed.\n("+r+": "+o+")");c.type=r,c.request=o,e[1](c)}i[t]=void 0}};var a=setTimeout(function(){c({type:"timeout",target:u})},12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(n)},s.m=t,s.c=r,s.d=function(t,n,e){s.o(t,n)||Object.defineProperty(t,n,{enumerable:!0,get:e})},s.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,n){if(1&n&&(t=s(t)),8&n)return t;if(4&n&&"object"==typeof t&&t&&t.__esModule)return t;var e=Object.create(null);if(s.r(e),Object.defineProperty(e,"default",{enumerable:!0,value:t}),2&n&&"string"!=typeof t)for(var r in t)s.d(e,r,function(n){return t[n]}.bind(null,r));return e},s.n=function(t){var n=t&&t.__esModule?function(){return t.default}:function(){return t};return s.d(n,"a",n),n},s.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)},s.p="/static/",s.oe=function(t){throw console.error(t),t};var u=window.webpackJsonp=window.webpackJsonp||[],a=u.push.bind(u);u.push=n,u=u.slice();for(var f=0;f<u.length;f++)n(u[f]);var l=a;return c.push([436,0]),e()}({1:function(t,n){var e=t.exports="undefined"!=typeof window&&window.Math==Math?window:"undefined"!=typeof self&&self.Math==Math?self:Function("return this")();"number"==typeof __g&&(__g=e)},10:function(t,n,e){var r=e(18),o=e(37);t.exports=e(12)?function(t,n,e){return r.f(t,n,o(1,e))}:function(t,n,e){return t[n]=e,t}},105:function(t,n,e){t.exports=e(113)},11:function(t,n,e){var r=e(1),o=e(4),i=e(22),c=e(10),s=e(16),u=function(t,n,e){var a,f,l,p=t&u.F,d=t&u.G,h=t&u.S,v=t&u.P,m=t&u.B,g=t&u.W,w=d?o:o[n]||(o[n]={}),y=w.prototype,b=d?r:h?r[n]:(r[n]||{}).prototype;for(a in d&&(e=n),e)(f=!p&&b&&void 0!==b[a])&&s(w,a)||(l=f?b[a]:e[a],w[a]=d&&"function"!=typeof b[a]?e[a]:m&&f?i(l,r):g&&b[a]==l?function(t){var n=function(n,e,r){if(this instanceof t){switch(arguments.length){case 0:return new t;case 1:return new t(n);case 2:return new t(n,e)}return new t(n,e,r)}return t.apply(this,arguments)};return n.prototype=t.prototype,n}(l):v&&"function"==typeof l?i(Function.call,l):l,v&&((w.virtual||(w.virtual={}))[a]=l,t&u.R&&y&&!y[a]&&c(y,a,l)))};u.F=1,u.G=2,u.S=4,u.P=8,u.B=16,u.W=32,u.U=64,u.R=128,t.exports=u},113:function(t,n,e){e(114),e(93),e(78),e(115),e(126),e(127),t.exports=e(4).Promise},114:function(t,n){},115:function(t,n,e){"use strict";var r,o,i,c,s=e(34),u=e(1),a=e(22),f=e(53),l=e(11),p=e(13),d=e(23),h=e(116),v=e(117),m=e(67),g=e(68).set,w=e(121)(),y=e(49),b=e(69),x=e(122),_=e(70),j=u.TypeError,S=u.process,$=S&&S.versions,k=$&&$.v8||"",O=u.Promise,P="process"==f(S),T=function(){},L=o=y.f,C=!!function(){try{var t=O.resolve(1),n=(t.constructor={})[e(3)("species")]=function(t){t(T,T)};return(P||"function"==typeof PromiseRejectionEvent)&&t.then(T)instanceof n&&0!==k.indexOf("6.6")&&-1===x.indexOf("Chrome/66")}catch(t){}}(),E=function(t){var n;return!(!p(t)||"function"!=typeof(n=t.then))&&n},M=function(t,n){if(!t._n){t._n=!0;var e=t._c;w(function(){for(var r=t._v,o=1==t._s,i=0,c=function(n){var e,i,c,s=o?n.ok:n.fail,u=n.resolve,a=n.reject,f=n.domain;try{s?(o||(2==t._h&&I(t),t._h=1),!0===s?e=r:(f&&f.enter(),e=s(r),f&&(f.exit(),c=!0)),e===n.promise?a(j("Promise-chain cycle")):(i=E(e))?i.call(e,u,a):u(e)):a(r)}catch(t){f&&!c&&f.exit(),a(t)}};e.length>i;)c(e[i++]);t._c=[],t._n=!1,n&&!t._h&&R(t)})}},R=function(t){g.call(u,function(){var n,e,r,o=t._v,i=A(t);if(i&&(n=b(function(){P?S.emit("unhandledRejection",o,t):(e=u.onunhandledrejection)?e({promise:t,reason:o}):(r=u.console)&&r.error&&r.error("Unhandled promise rejection",o)}),t._h=P||A(t)?2:1),t._a=void 0,i&&n.e)throw n.v})},A=function(t){return 1!==t._h&&0===(t._a||t._c).length},I=function(t){g.call(u,function(){var n;P?S.emit("rejectionHandled",t):(n=u.onrejectionhandled)&&n({promise:t,reason:t._v})})},N=function(t){var n=this;n._d||(n._d=!0,(n=n._w||n)._v=t,n._s=2,n._a||(n._a=n._c.slice()),M(n,!0))},F=function(t){var n,e=this;if(!e._d){e._d=!0,e=e._w||e;try{if(e===t)throw j("Promise can't be resolved itself");(n=E(t))?w(function(){var r={_w:e,_d:!1};try{n.call(t,a(F,r,1),a(N,r,1))}catch(t){N.call(r,t)}}):(e._v=t,e._s=1,M(e,!1))}catch(t){N.call({_w:e,_d:!1},t)}}};C||(O=function(t){h(this,O,"Promise","_h"),d(t),r.call(this);try{t(a(F,this,1),a(N,this,1))}catch(t){N.call(this,t)}},(r=function(t){this._c=[],this._a=void 0,this._s=0,this._d=!1,this._v=void 0,this._h=0,this._n=!1}).prototype=e(123)(O.prototype,{then:function(t,n){var e=L(m(this,O));return e.ok="function"!=typeof t||t,e.fail="function"==typeof n&&n,e.domain=P?S.domain:void 0,this._c.push(e),this._a&&this._a.push(e),this._s&&M(this,!1),e.promise},catch:function(t){return this.then(void 0,t)}}),i=function(){var t=new r;this.promise=t,this.resolve=a(F,t,1),this.reject=a(N,t,1)},y.f=L=function(t){return t===O||t===c?new i(t):o(t)}),l(l.G+l.W+l.F*!C,{Promise:O}),e(35)(O,"Promise"),e(124)("Promise"),c=e(4).Promise,l(l.S+l.F*!C,"Promise",{reject:function(t){var n=L(this);return(0,n.reject)(t),n.promise}}),l(l.S+l.F*(s||!C),"Promise",{resolve:function(t){return _(s&&this===c?O:this,t)}}),l(l.S+l.F*!(C&&e(125)(function(t){O.all(t).catch(T)})),"Promise",{all:function(t){var n=this,e=L(n),r=e.resolve,o=e.reject,i=b(function(){var e=[],i=0,c=1;v(t,!1,function(t){var s=i++,u=!1;e.push(void 0),c++,n.resolve(t).then(function(t){u||(u=!0,e[s]=t,--c||r(e))},o)}),--c||r(e)});return i.e&&o(i.v),e.promise},race:function(t){var n=this,e=L(n),r=e.reject,o=b(function(){v(t,!1,function(t){n.resolve(t).then(e.resolve,r)})});return o.e&&r(o.v),e.promise}})},116:function(t,n){t.exports=function(t,n,e,r){if(!(t instanceof n)||void 0!==r&&r in t)throw TypeError(e+": incorrect invocation!");return t}},117:function(t,n,e){var r=e(22),o=e(118),i=e(119),c=e(5),s=e(51),u=e(95),a={},f={};(n=t.exports=function(t,n,e,l,p){var d,h,v,m,g=p?function(){return t}:u(t),w=r(e,l,n?2:1),y=0;if("function"!=typeof g)throw TypeError(t+" is not iterable!");if(i(g)){for(d=s(t.length);d>y;y++)if((m=n?w(c(h=t[y])[0],h[1]):w(t[y]))===a||m===f)return m}else for(v=g.call(t);!(h=v.next()).done;)if((m=o(v,w,h.value,n))===a||m===f)return m}).BREAK=a,n.RETURN=f},118:function(t,n,e){var r=e(5);t.exports=function(t,n,e,o){try{return o?n(r(e)[0],e[1]):n(e)}catch(n){var i=t.return;throw void 0!==i&&r(i.call(t)),n}}},119:function(t,n,e){var r=e(15),o=e(3)("iterator"),i=Array.prototype;t.exports=function(t){return void 0!==t&&(r.Array===t||i[o]===t)}},12:function(t,n,e){t.exports=!e(24)(function(){return 7!=Object.defineProperty({},"a",{get:function(){return 7}}).a})},120:function(t,n){t.exports=function(t,n,e){var r=void 0===e;switch(n.length){case 0:return r?t():t.call(e);case 1:return r?t(n[0]):t.call(e,n[0]);case 2:return r?t(n[0],n[1]):t.call(e,n[0],n[1]);case 3:return r?t(n[0],n[1],n[2]):t.call(e,n[0],n[1],n[2]);case 4:return r?t(n[0],n[1],n[2],n[3]):t.call(e,n[0],n[1],n[2],n[3])}return t.apply(e,n)}},121:function(t,n,e){var r=e(1),o=e(68).set,i=r.MutationObserver||r.WebKitMutationObserver,c=r.process,s=r.Promise,u="process"==e(25)(c);t.exports=function(){var t,n,e,a=function(){var r,o;for(u&&(r=c.domain)&&r.exit();t;){o=t.fn,t=t.next;try{o()}catch(r){throw t?e():n=void 0,r}}n=void 0,r&&r.enter()};if(u)e=function(){c.nextTick(a)};else if(!i||r.navigator&&r.navigator.standalone)if(s&&s.resolve){var f=s.resolve(void 0);e=function(){f.then(a)}}else e=function(){o.call(r,a)};else{var l=!0,p=document.createTextNode("");new i(a).observe(p,{characterData:!0}),e=function(){p.data=l=!l}}return function(r){var o={fn:r,next:void 0};n&&(n.next=o),t||(t=o,e()),n=o}}},122:function(t,n,e){var r=e(1).navigator;t.exports=r&&r.userAgent||""},123:function(t,n,e){var r=e(10);t.exports=function(t,n,e){for(var o in n)e&&t[o]?t[o]=n[o]:r(t,o,n[o]);return t}},124:function(t,n,e){"use strict";var r=e(1),o=e(4),i=e(18),c=e(12),s=e(3)("species");t.exports=function(t){var n="function"==typeof o[t]?o[t]:r[t];c&&n&&!n[s]&&i.f(n,s,{configurable:!0,get:function(){return this}})}},125:function(t,n,e){var r=e(3)("iterator"),o=!1;try{var i=[7][r]();i.return=function(){o=!0},Array.from(i,function(){throw 2})}catch(t){}t.exports=function(t,n){if(!n&&!o)return!1;var e=!1;try{var i=[7],c=i[r]();c.next=function(){return{done:e=!0}},i[r]=function(){return c},t(i)}catch(t){}return e}},126:function(t,n,e){"use strict";var r=e(11),o=e(4),i=e(1),c=e(67),s=e(70);r(r.P+r.R,"Promise",{finally:function(t){var n=c(this,o.Promise||i.Promise),e="function"==typeof t;return this.then(e?function(e){return s(n,t()).then(function(){return e})}:t,e?function(e){return s(n,t()).then(function(){throw e})}:t)}})},127:function(t,n,e){"use strict";var r=e(11),o=e(49),i=e(69);r(r.S,"Promise",{try:function(t){var n=o.f(this),e=i(t);return(e.e?n.reject:n.resolve)(e.v),n.promise}})},13:function(t,n){t.exports=function(t){return"object"==typeof t?null!==t:"function"==typeof t}},144:function(t,n,e){var r=function(){return this||"object"==typeof self&&self}()||Function("return this")(),o=r.regeneratorRuntime&&Object.getOwnPropertyNames(r).indexOf("regeneratorRuntime")>=0,i=o&&r.regeneratorRuntime;if(r.regeneratorRuntime=void 0,t.exports=e(145),o)r.regeneratorRuntime=i;else try{delete r.regeneratorRuntime}catch(t){r.regeneratorRuntime=void 0}},15:function(t,n){t.exports={}},16:function(t,n){var e={}.hasOwnProperty;t.exports=function(t,n){return e.call(t,n)}},17:function(t,n,e){t.exports=e(74)},18:function(t,n,e){var r=e(5),o=e(59),i=e(60),c=Object.defineProperty;n.f=e(12)?Object.defineProperty:function(t,n,e){if(r(t),n=i(n,!0),r(e),o)try{return c(t,n,e)}catch(t){}if("get"in e||"set"in e)throw TypeError("Accessors not supported!");return"value"in e&&(t[n]=e.value),t}},19:function(t,n){t.exports=function(t){if(null==t)throw TypeError("Can't call method on  "+t);return t}},2:function(t,n,e){"use strict";function r(t){if(!t.ok)throw t;return t}function o(t){for(var n=0;n<t.length;++n)if(!t[n].ok)throw t[n];return t}function i(t){return"/static/"+t}function c(t,n,e){return void 0===n&&(n={}),void 0===e&&(e=null),n["X-CSRFToken"]=Cookies.get("csrftoken"),fetch(t,{credentials:"include",headers:n,method:"POST",body:e})}function s(t,n){return new RegExp("(?:git|https?|git@)(?:\\:\\/\\/)?"+n+"[/|:][A-Za-z0-9-]+?\\/[\\w\\.-]+\\/?(?!=.git)(?:\\.git(?:\\/?|\\#[\\w\\.\\-_]+)?)?$").test(t)}function u(){history.replaceState("",document.title,window.location.pathname+window.location.search)}e.d(n,"b",function(){return r}),e.d(n,"c",function(){return o}),e.d(n,"f",function(){return i}),e.d(n,"a",function(){return c}),e.d(n,"d",function(){return s}),e.d(n,"e",function(){return u})},217:function(t,n,e){"use strict";
/*! npm.im/object-fit-images 3.2.4 */var r="bfred-it:object-fit-images",o=/(object-fit|object-position)\s*:\s*([-.\w\s%]+)/g,i="undefined"==typeof Image?{style:{"object-position":1}}:new Image,c="object-fit"in i.style,s="object-position"in i.style,u="background-size"in i.style,a="string"==typeof i.currentSrc,f=i.getAttribute,l=i.setAttribute,p=!1;function d(t,n,e){var r="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='"+(n||1)+"' height='"+(e||0)+"'%3E%3C/svg%3E";f.call(t,"src")!==r&&l.call(t,"src",r)}function h(t,n){t.naturalWidth?n(t):setTimeout(h,100,t,n)}function v(t){var n=function(t){for(var n,e=getComputedStyle(t).fontFamily,r={};null!==(n=o.exec(e));)r[n[1]]=n[2];return r}(t),e=t[r];if(n["object-fit"]=n["object-fit"]||"fill",!e.img){if("fill"===n["object-fit"])return;if(!e.skipTest&&c&&!n["object-position"])return}if(!e.img){e.img=new Image(t.width,t.height),e.img.srcset=f.call(t,"data-ofi-srcset")||t.srcset,e.img.src=f.call(t,"data-ofi-src")||t.src,l.call(t,"data-ofi-src",t.src),t.srcset&&l.call(t,"data-ofi-srcset",t.srcset),d(t,t.naturalWidth||t.width,t.naturalHeight||t.height),t.srcset&&(t.srcset="");try{!function(t){var n={get:function(n){return t[r].img[n||"src"]},set:function(n,e){return t[r].img[e||"src"]=n,l.call(t,"data-ofi-"+e,n),v(t),n}};Object.defineProperty(t,"src",n),Object.defineProperty(t,"currentSrc",{get:function(){return n.get("currentSrc")}}),Object.defineProperty(t,"srcset",{get:function(){return n.get("srcset")},set:function(t){return n.set(t,"srcset")}})}(t)}catch(t){window.console&&console.warn("https://bit.ly/ofi-old-browser")}}!function(t){if(t.srcset&&!a&&window.picturefill){var n=window.picturefill._;t[n.ns]&&t[n.ns].evaled||n.fillImg(t,{reselect:!0}),t[n.ns].curSrc||(t[n.ns].supported=!1,n.fillImg(t,{reselect:!0})),t.currentSrc=t[n.ns].curSrc||t.src}}(e.img),t.style.backgroundImage='url("'+(e.img.currentSrc||e.img.src).replace(/"/g,'\\"')+'")',t.style.backgroundPosition=n["object-position"]||"center",t.style.backgroundRepeat="no-repeat",t.style.backgroundOrigin="content-box",/scale-down/.test(n["object-fit"])?h(e.img,function(){e.img.naturalWidth>t.width||e.img.naturalHeight>t.height?t.style.backgroundSize="contain":t.style.backgroundSize="auto"}):t.style.backgroundSize=n["object-fit"].replace("none","auto").replace("fill","100% 100%"),h(e.img,function(n){d(t,n.naturalWidth,n.naturalHeight)})}function m(t,n){var e=!p&&!t;if(n=n||{},t=t||"img",s&&!n.skipTest||!u)return!1;"img"===t?t=document.getElementsByTagName("img"):"string"==typeof t?t=document.querySelectorAll(t):"length"in t||(t=[t]);for(var o=0;o<t.length;o++)t[o][r]=t[o][r]||{skipTest:n.skipTest},v(t[o]);e&&(document.body.addEventListener("load",function(t){"IMG"===t.target.tagName&&m(t.target,{skipTest:n.skipTest})},!0),p=!0,t="img"),n.watchMQ&&window.addEventListener("resize",m.bind(null,t,{skipTest:n.skipTest}))}m.supportsObjectFit=c,m.supportsObjectPosition=s,function(){function t(t,n){return t[r]&&t[r].img&&("src"===n||"srcset"===n)?t[r].img:t}s||(HTMLImageElement.prototype.getAttribute=function(n){return f.call(t(this,n),n)},HTMLImageElement.prototype.setAttribute=function(n,e){return l.call(t(this,n),n,String(e))})}(),t.exports=m},22:function(t,n,e){var r=e(23);t.exports=function(t,n,e){if(r(t),void 0===n)return t;switch(e){case 1:return function(e){return t.call(n,e)};case 2:return function(e,r){return t.call(n,e,r)};case 3:return function(e,r,o){return t.call(n,e,r,o)}}return function(){return t.apply(n,arguments)}}},23:function(t,n){t.exports=function(t){if("function"!=typeof t)throw TypeError(t+" is not a function!");return t}},24:function(t,n){t.exports=function(t){try{return!!t()}catch(t){return!0}}},25:function(t,n){var e={}.toString;t.exports=function(t){return e.call(t).slice(8,-1)}},28:function(t,n,e){var r=e(13),o=e(1).document,i=r(o)&&r(o.createElement);t.exports=function(t){return i?o.createElement(t):{}}},29:function(t,n,e){var r=e(82),o=e(19);t.exports=function(t){return r(o(t))}},3:function(t,n,e){var r=e(46)("wks"),o=e(47),i=e(1).Symbol,c="function"==typeof i;(t.exports=function(t){return r[t]||(r[t]=c&&i[t]||(c?i:o)("Symbol."+t))}).store=r},30:function(t,n){var e=Math.ceil,r=Math.floor;t.exports=function(t){return isNaN(t=+t)?0:(t>0?r:e)(t)}},31:function(t,n,e){var r=e(46)("keys"),o=e(47);t.exports=function(t){return r[t]||(r[t]=o(t))}},32:function(t,n,e){t.exports=e(73)},33:function(t,n,e){t.exports=e(144)},34:function(t,n){t.exports=!0},35:function(t,n,e){var r=e(18).f,o=e(16),i=e(3)("toStringTag");t.exports=function(t,n,e){t&&!o(t=e?t:t.prototype,i)&&r(t,i,{configurable:!0,value:n})}},37:function(t,n){t.exports=function(t,n){return{enumerable:!(1&t),configurable:!(2&t),writable:!(4&t),value:n}}},4:function(t,n){var e=t.exports={version:"2.6.4"};"number"==typeof __e&&(__e=e)},436:function(t,n,e){t.exports=e(440)},437:function(t,n,e){},438:function(t,n,e){},44:function(t,n){t.exports="\t\n\v\f\r   ᠎             　\u2028\u2029\ufeff"},440:function(t,n,e){"use strict";e.r(n);e(178),e(437),e(438);var r,o,i=e(32),c=e.n(i),s=e(217),u=e.n(s),a=e(172),f=!1,l=localStorage.getItem("swh-sidebar-collapsed");function p(){$("body").css("padding-bottom",$("footer").outerHeight()+"px")}function d(t){$(document).ready(function(){$(".swh-"+t+"-item").addClass("active"),$(".swh-"+t+"-link").addClass("active"),$(window).on("unload",function(){var n=$("body").hasClass("sidebar-collapse");localStorage.setItem("swh-sidebar-collapsed",c()(n)),"browse"===t&&sessionStorage.setItem("last-browse-page",window.location)})})}function h(t,n){$("#swh-web-modal-message .modal-title").text(t),$("#swh-web-modal-message .modal-content p").text(n),$("#swh-web-modal-message").modal("show")}function v(t,n,e){$("#swh-web-modal-confirm .modal-title").text(t),$("#swh-web-modal-confirm .modal-content p").text(n),$("#swh-web-modal-confirm #swh-web-modal-confirm-ok-btn").bind("click",function(){e(),$("#swh-web-modal-confirm").modal("hide"),$("#swh-web-modal-confirm #swh-web-modal-confirm-ok-btn").unbind("click")}),$("#swh-web-modal-confirm").modal("show")}function m(t){r=t}function g(t){return r[t]}function w(t){$(t).on("click",function(){return window.location=$(this).data("href"),!1}),$("td > a").on("click",function(t){t.stopPropagation()})}function y(t){o=t}function b(){return o}void 0!==l&&(f=JSON.parse(l)),a.Layout.prototype.fixLayoutHeight=function(){var t=$(window).height(),n=$(".main-header").outerHeight(),e=$(".footer").outerHeight(),r=($(".main-sidebar").height(),$(".swh-top-bar").height());$(".content-wrapper").css("min-height",t-r-n-e-10),$(".main-sidebar").css("min-height",t-r-n-e-10)},$(document).on("DOMContentLoaded",function(){if(f){var t=$(".main-sidebar, .main-sidebar:before").css("transition"),n=$(".sidebar .nav-link p, .main-sidebar .brand-text, .sidebar .user-panel .info").css("transition");$(".main-sidebar, .main-sidebar:before").css("transition","none"),$(".sidebar .nav-link p, .main-sidebar .brand-text, .sidebar .user-panel .info").css("transition","none"),$("body").addClass("sidebar-collapse"),$(".swh-words-logo-swh").css("visibility","visible"),setTimeout(function(){$(".main-sidebar, .main-sidebar:before").css("transition",t),$(".sidebar .nav-link p, .main-sidebar .brand-text, .sidebar .user-panel .info").css("transition",n)})}}),$(document).on("collapsed.lte.pushmenu",function(t){$("body").width()>980&&$(".swh-words-logo-swh").css("visibility","visible")}),$(document).on("shown.lte.pushmenu",function(t){$(".swh-words-logo-swh").css("visibility","hidden")}),$(document).ready(function(){$(".swh-browse-link").click(function(t){var n=sessionStorage.getItem("last-browse-page");n&&(t.preventDefault(),window.location=n)}),p(),$(window).resize(function(){p(),$("body").hasClass("sidebar-collapse")&&$("body").width()>980&&$(".swh-words-logo-swh").css("visibility","visible")}),u()(),$(".swh-browse-top-navigation").append($(".modal"))});var x=e(33),_=e.n(x),j=e(17),S=e.n(j),k=e(58),O=e.n(k),P=e(2);function T(t){return L.apply(this,arguments)}function L(){return(L=O()(_.a.mark(function t(n){var r,o,i,c,s,u;return _.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return u=function(){for(var t=[],n=new RegExp(/L(\d+)/g),e=n.exec(window.location.hash);e;)t.push(S()(e[1])),e=n.exec(window.location.hash);if(c(),1===t.length)r=S()(t[0]),s(i(t[0]));else if(t[0]<t[t.length-1]){r=S()(t[0]),s(i(t[0]));for(var o=t[0]+1;o<=t[t.length-1];++o)i(o)}},s=function(t){$(t).closest(".swh-content").length>0&&$("html, body").animate({scrollTop:$(t).offset().top-70},500)},c=function(){r=null,$(".hljs-ln-line[data-line-number]").css("background-color","inherit")},i=function(t){var n=$('.hljs-ln-line[data-line-number="'+t+'"]');return n.css("background-color",o),n},void 0===n&&(n=!0),t.next=7,Promise.all([e.e(0),e.e(3)]).then(e.bind(null,646));case 7:r=null,o="rgb(193, 255, 193)",$(document).ready(function(){$("code").each(function(t,e){hljs.highlightBlock(e),n&&hljs.lineNumbersBlock(e)}),n&&($("body").click(function(t){if(t.target.classList.contains("hljs-ln-n")){var n=S()($(t.target).data("line-number"));if(t.shiftKey&&r&&n>r){var e=r;c();for(var o=e;o<=n;++o)i(o);r=e,window.location.hash="#L"+e+"-L"+n}else c(),i(n),window.location.hash="#L"+n,s(t.target)}else $(t.target).closest(".hljs").length&&(c(),Object(P.e)())}),$(window).on("hashchange",function(){return u()}),setTimeout(function(){u()}))});case 10:case"end":return t.stop()}},t,this)}))).apply(this,arguments)}function C(t,n){return E.apply(this,arguments)}function E(){return(E=O()(_.a.mark(function t(n,r){var o;return _.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.e(8).then(e.bind(null,647));case 2:o=t.sent,$(document).ready(function(){var t=new o.Converter({tables:!0});fetch(r).then(P.b).then(function(t){return t.text()}).then(function(e){$(n).addClass("swh-showdown"),$(n).html(t.makeHtml(e))}).catch(function(){$(n).text("Readme bytes are not available")})});case 4:case"end":return t.stop()}},t,this)}))).apply(this,arguments)}function M(t,n){return R.apply(this,arguments)}function R(){return(R=O()(_.a.mark(function t(n,r){var o,i,c,s;return _.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.e(4).then(e.bind(null,648));case 2:o=t.sent,i=new o.Parser,c=i.parse(r,{toc:!1}),s=c.convert(o.ConverterHTML,{}),$(n).addClass("swh-org"),$(n).html(s.toString()),$(".swh-org ul").first().remove(),$(".section-number").remove();case 10:case"end":return t.stop()}},t,this)}))).apply(this,arguments)}function A(t,n){$(document).ready(function(){fetch(n).then(P.b).then(function(t){return t.text()}).then(function(n){M(t,n)}).catch(function(){$(t).text("Readme bytes are not available")})})}function I(t,n){$(document).ready(function(){fetch(n).then(P.b).then(function(t){return t.text()}).then(function(n){-1!==n.indexOf("-*- mode: org -*-")?M(t,n.replace("-*- mode: org -*-","")):($(t).addClass("swh-readme-txt"),$(t).html("<pre>"+n+"</pre>"))}).catch(function(){$(t).text("Readme bytes are not available")})})}function N(t){return F.apply(this,arguments)}function F(){return(F=O()(_.a.mark(function t(n){var r,o,i,c,s,u,a,f,l,p,d,h;return _.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return d=function(){o>=r.numPages||l(++o)},p=function(){o<=1||l(--o)},l=function(t){i?c=t:f(t)},f=function(t){i=!0,r.getPage(t).then(function(t){var n=t.getViewport(s);u.width=n.width,u.height=n.height;var e={canvasContext:a,viewport:n};t.render(e).promise.then(function(){i=!1,null!==c&&(f(c),c=null)})}),$("#pdf-page-num").text(t)},r=null,o=1,i=!1,c=null,s=1.5,u=$("#pdf-canvas")[0],a=u.getContext("2d"),t.next=13,e.e(6).then(e.t.bind(null,649,7));case 13:(h=t.sent).GlobalWorkerOptions.workerSrc=Object(P.f)("js/pdf.worker.min.js"),$(document).ready(function(){$("#pdf-prev").click(p),$("#pdf-next").click(d),h.getDocument(n).promise.then(function(t){r=t,$("#pdf-page-count").text(r.numPages),f(o)},function(t){console.error(t)})});case 16:case"end":return t.stop()}},t,this)}))).apply(this,arguments)}e.d(n,"initPage",function(){return d}),e.d(n,"showModalMessage",function(){return h}),e.d(n,"showModalConfirm",function(){return v}),e.d(n,"setSwhObjectIcons",function(){return m}),e.d(n,"getSwhObjectIcon",function(){return g}),e.d(n,"initTableRowLinks",function(){return w}),e.d(n,"setReCaptchaActivated",function(){return y}),e.d(n,"isReCaptchaActivated",function(){return b}),e.d(n,"highlightCode",function(){return T}),e.d(n,"renderMarkdown",function(){return C}),e.d(n,"renderOrgData",function(){return M}),e.d(n,"renderOrg",function(){return A}),e.d(n,"renderTxt",function(){return I}),e.d(n,"renderPdf",function(){return N})},45:function(t,n,e){"use strict";var r=e(34),o=e(11),i=e(83),c=e(10),s=e(15),u=e(84),a=e(35),f=e(91),l=e(3)("iterator"),p=!([].keys&&"next"in[].keys()),d=function(){return this};t.exports=function(t,n,e,h,v,m,g){u(e,n,h);var w,y,b,x=function(t){if(!p&&t in $)return $[t];switch(t){case"keys":case"values":return function(){return new e(this,t)}}return function(){return new e(this,t)}},_=n+" Iterator",j="values"==v,S=!1,$=t.prototype,k=$[l]||$["@@iterator"]||v&&$[v],O=k||x(v),P=v?j?x("entries"):O:void 0,T="Array"==n&&$.entries||k;if(T&&(b=f(T.call(new t)))!==Object.prototype&&b.next&&(a(b,_,!0),r||"function"==typeof b[l]||c(b,l,d)),j&&k&&"values"!==k.name&&(S=!0,O=function(){return k.call(this)}),r&&!g||!p&&!S&&$[l]||c($,l,O),s[n]=O,s[_]=d,v)if(w={values:j?O:x("values"),keys:m?O:x("keys"),entries:P},g)for(y in w)y in $||i($,y,w[y]);else o(o.P+o.F*(p||S),n,w);return w}},46:function(t,n,e){var r=e(4),o=e(1),i=o["__core-js_shared__"]||(o["__core-js_shared__"]={});(t.exports=function(t,n){return i[t]||(i[t]=void 0!==n?n:{})})("versions",[]).push({version:r.version,mode:e(34)?"pure":"global",copyright:"© 2019 Denis Pushkarev (zloirock.ru)"})},47:function(t,n){var e=0,r=Math.random();t.exports=function(t){return"Symbol(".concat(void 0===t?"":t,")_",(++e+r).toString(36))}},48:function(t,n){t.exports="constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")},49:function(t,n,e){"use strict";var r=e(23);function o(t){var n,e;this.promise=new t(function(t,r){if(void 0!==n||void 0!==e)throw TypeError("Bad Promise constructor");n=t,e=r}),this.resolve=r(n),this.reject=r(e)}t.exports.f=function(t){return new o(t)}},5:function(t,n,e){var r=e(13);t.exports=function(t){if(!r(t))throw TypeError(t+" is not an object!");return t}},51:function(t,n,e){var r=e(30),o=Math.min;t.exports=function(t){return t>0?o(r(t),9007199254740991):0}},52:function(t,n,e){var r=e(1).document;t.exports=r&&r.documentElement},53:function(t,n,e){var r=e(25),o=e(3)("toStringTag"),i="Arguments"==r(function(){return arguments}());t.exports=function(t){var n,e,c;return void 0===t?"Undefined":null===t?"Null":"string"==typeof(e=function(t,n){try{return t[n]}catch(t){}}(n=Object(t),o))?e:i?r(n):"Object"==(c=r(n))&&"function"==typeof n.callee?"Arguments":c}},58:function(t,n,e){var r=e(105);function o(t,n,e,o,i,c,s){try{var u=t[c](s),a=u.value}catch(t){return void e(t)}u.done?n(a):r.resolve(a).then(o,i)}t.exports=function(t){return function(){var n=this,e=arguments;return new r(function(r,i){var c=t.apply(n,e);function s(t){o(c,r,i,s,u,"next",t)}function u(t){o(c,r,i,s,u,"throw",t)}s(void 0)})}}},59:function(t,n,e){t.exports=!e(12)&&!e(24)(function(){return 7!=Object.defineProperty(e(28)("div"),"a",{get:function(){return 7}}).a})},60:function(t,n,e){var r=e(13);t.exports=function(t,n){if(!r(t))return t;var e,o;if(n&&"function"==typeof(e=t.toString)&&!r(o=e.call(t)))return o;if("function"==typeof(e=t.valueOf)&&!r(o=e.call(t)))return o;if(!n&&"function"==typeof(e=t.toString)&&!r(o=e.call(t)))return o;throw TypeError("Can't convert object to primitive value")}},67:function(t,n,e){var r=e(5),o=e(23),i=e(3)("species");t.exports=function(t,n){var e,c=r(t).constructor;return void 0===c||null==(e=r(c)[i])?n:o(e)}},68:function(t,n,e){var r,o,i,c=e(22),s=e(120),u=e(52),a=e(28),f=e(1),l=f.process,p=f.setImmediate,d=f.clearImmediate,h=f.MessageChannel,v=f.Dispatch,m=0,g={},w=function(){var t=+this;if(g.hasOwnProperty(t)){var n=g[t];delete g[t],n()}},y=function(t){w.call(t.data)};p&&d||(p=function(t){for(var n=[],e=1;arguments.length>e;)n.push(arguments[e++]);return g[++m]=function(){s("function"==typeof t?t:Function(t),n)},r(m),m},d=function(t){delete g[t]},"process"==e(25)(l)?r=function(t){l.nextTick(c(w,t,1))}:v&&v.now?r=function(t){v.now(c(w,t,1))}:h?(i=(o=new h).port2,o.port1.onmessage=y,r=c(i.postMessage,i,1)):f.addEventListener&&"function"==typeof postMessage&&!f.importScripts?(r=function(t){f.postMessage(t+"","*")},f.addEventListener("message",y,!1)):r="onreadystatechange"in a("script")?function(t){u.appendChild(a("script")).onreadystatechange=function(){u.removeChild(this),w.call(t)}}:function(t){setTimeout(c(w,t,1),0)}),t.exports={set:p,clear:d}},69:function(t,n){t.exports=function(t){try{return{e:!1,v:t()}}catch(t){return{e:!0,v:t}}}},70:function(t,n,e){var r=e(5),o=e(13),i=e(49);t.exports=function(t,n){if(r(t),o(n)&&n.constructor===t)return n;var e=i.f(t);return(0,e.resolve)(n),e.promise}},73:function(t,n,e){var r=e(4),o=r.JSON||(r.JSON={stringify:JSON.stringify});t.exports=function(t){return o.stringify.apply(o,arguments)}},74:function(t,n,e){e(75),t.exports=e(4).parseInt},75:function(t,n,e){var r=e(11),o=e(76);r(r.G+r.F*(parseInt!=o),{parseInt:o})},76:function(t,n,e){var r=e(1).parseInt,o=e(77).trim,i=e(44),c=/^[-+]?0[xX]/;t.exports=8!==r(i+"08")||22!==r(i+"0x16")?function(t,n){var e=o(String(t),3);return r(e,n>>>0||(c.test(e)?16:10))}:r},77:function(t,n,e){var r=e(11),o=e(19),i=e(24),c=e(44),s="["+c+"]",u=RegExp("^"+s+s+"*"),a=RegExp(s+s+"*$"),f=function(t,n,e){var o={},s=i(function(){return!!c[t]()||"​"!="​"[t]()}),u=o[t]=s?n(l):c[t];e&&(o[e]=u),r(r.P+r.F*s,"String",o)},l=f.trim=function(t,n){return t=String(o(t)),1&n&&(t=t.replace(u,"")),2&n&&(t=t.replace(a,"")),t};t.exports=f},78:function(t,n,e){e(79);for(var r=e(1),o=e(10),i=e(15),c=e(3)("toStringTag"),s="CSSRuleList,CSSStyleDeclaration,CSSValueList,ClientRectList,DOMRectList,DOMStringList,DOMTokenList,DataTransferItemList,FileList,HTMLAllCollection,HTMLCollection,HTMLFormElement,HTMLSelectElement,MediaList,MimeTypeArray,NamedNodeMap,NodeList,PaintRequestList,Plugin,PluginArray,SVGLengthList,SVGNumberList,SVGPathSegList,SVGPointList,SVGStringList,SVGTransformList,SourceBufferList,StyleSheetList,TextTrackCueList,TextTrackList,TouchList".split(","),u=0;u<s.length;u++){var a=s[u],f=r[a],l=f&&f.prototype;l&&!l[c]&&o(l,c,a),i[a]=i.Array}},79:function(t,n,e){"use strict";var r=e(80),o=e(81),i=e(15),c=e(29);t.exports=e(45)(Array,"Array",function(t,n){this._t=c(t),this._i=0,this._k=n},function(){var t=this._t,n=this._k,e=this._i++;return!t||e>=t.length?(this._t=void 0,o(1)):o(0,"keys"==n?e:"values"==n?t[e]:[e,t[e]])},"values"),i.Arguments=i.Array,r("keys"),r("values"),r("entries")},80:function(t,n){t.exports=function(){}},81:function(t,n){t.exports=function(t,n){return{value:n,done:!!t}}},82:function(t,n,e){var r=e(25);t.exports=Object("z").propertyIsEnumerable(0)?Object:function(t){return"String"==r(t)?t.split(""):Object(t)}},83:function(t,n,e){t.exports=e(10)},84:function(t,n,e){"use strict";var r=e(85),o=e(37),i=e(35),c={};e(10)(c,e(3)("iterator"),function(){return this}),t.exports=function(t,n,e){t.prototype=r(c,{next:o(1,e)}),i(t,n+" Iterator")}},85:function(t,n,e){var r=e(5),o=e(86),i=e(48),c=e(31)("IE_PROTO"),s=function(){},u=function(){var t,n=e(28)("iframe"),r=i.length;for(n.style.display="none",e(52).appendChild(n),n.src="javascript:",(t=n.contentWindow.document).open(),t.write("<script>document.F=Object<\/script>"),t.close(),u=t.F;r--;)delete u.prototype[i[r]];return u()};t.exports=Object.create||function(t,n){var e;return null!==t?(s.prototype=r(t),e=new s,s.prototype=null,e[c]=t):e=u(),void 0===n?e:o(e,n)}},86:function(t,n,e){var r=e(18),o=e(5),i=e(87);t.exports=e(12)?Object.defineProperties:function(t,n){o(t);for(var e,c=i(n),s=c.length,u=0;s>u;)r.f(t,e=c[u++],n[e]);return t}},87:function(t,n,e){var r=e(88),o=e(48);t.exports=Object.keys||function(t){return r(t,o)}},88:function(t,n,e){var r=e(16),o=e(29),i=e(89)(!1),c=e(31)("IE_PROTO");t.exports=function(t,n){var e,s=o(t),u=0,a=[];for(e in s)e!=c&&r(s,e)&&a.push(e);for(;n.length>u;)r(s,e=n[u++])&&(~i(a,e)||a.push(e));return a}},89:function(t,n,e){var r=e(29),o=e(51),i=e(90);t.exports=function(t){return function(n,e,c){var s,u=r(n),a=o(u.length),f=i(c,a);if(t&&e!=e){for(;a>f;)if((s=u[f++])!=s)return!0}else for(;a>f;f++)if((t||f in u)&&u[f]===e)return t||f||0;return!t&&-1}}},90:function(t,n,e){var r=e(30),o=Math.max,i=Math.min;t.exports=function(t,n){return(t=r(t))<0?o(t+n,0):i(t,n)}},91:function(t,n,e){var r=e(16),o=e(92),i=e(31)("IE_PROTO"),c=Object.prototype;t.exports=Object.getPrototypeOf||function(t){return t=o(t),r(t,i)?t[i]:"function"==typeof t.constructor&&t instanceof t.constructor?t.constructor.prototype:t instanceof Object?c:null}},92:function(t,n,e){var r=e(19);t.exports=function(t){return Object(r(t))}},93:function(t,n,e){"use strict";var r=e(94)(!0);e(45)(String,"String",function(t){this._t=String(t),this._i=0},function(){var t,n=this._t,e=this._i;return e>=n.length?{value:void 0,done:!0}:(t=r(n,e),this._i+=t.length,{value:t,done:!1})})},94:function(t,n,e){var r=e(30),o=e(19);t.exports=function(t){return function(n,e){var i,c,s=String(o(n)),u=r(e),a=s.length;return u<0||u>=a?t?"":void 0:(i=s.charCodeAt(u))<55296||i>56319||u+1===a||(c=s.charCodeAt(u+1))<56320||c>57343?t?s.charAt(u):i:t?s.slice(u,u+2):c-56320+(i-55296<<10)+65536}}},95:function(t,n,e){var r=e(53),o=e(3)("iterator"),i=e(15);t.exports=e(4).getIteratorMethod=function(t){if(null!=t)return t[o]||t["@@iterator"]||i[r(t)]}}})});
//# webapp.658e0d86685e99c6d95f.js.map