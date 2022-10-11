(()=>{"use strict";var e,t={533:function(e,t,o){var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var r=n(o(5311)),a=o(9408);window.ModalWorkflow=function(e){var t={},o=e.responses||{},n=e.onError||function(){};(0,r.default)("body > .modal").remove(),t.triggerElement=document.activeElement,t.triggerElement.setAttribute("disabled",!0);var i=(0,r.default)('<div class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <button type="button" class="button close button--icon text-replace" data-dismiss="modal"><svg class="icon icon-cross" aria-hidden="true"><use href="#icon-cross"></use></svg>'+(0,a.gettext)("Close")+'</button>\n      <div class="modal-body"></div>\n    </div>\x3c!-- /.modal-content --\x3e\n  </div>\x3c!-- /.modal-dialog --\x3e\n</div>');return(0,r.default)("body").append(i),i.modal("hide"),i.on("hide.bs.modal",(function(){t.triggerElement.removeAttribute("disabled")})),i.on("hidden.bs.modal",(function(){t.triggerElement.focus(),i.remove()})),t.body=i.find(".modal-body"),t.loadUrl=function(e,o){r.default.get(e,o,t.loadResponseText,"text").fail(n)},t.postForm=function(e,o){r.default.post(e,o,t.loadResponseText,"text").fail(n)},t.ajaxifyForm=function(e){(0,r.default)(e).each((function(){var e=this.action;"get"===this.method.toLowerCase()?(0,r.default)(this).on("submit",(function(){return t.loadUrl(e,(0,r.default)(this).serialize()),!1})):(0,r.default)(this).on("submit",(function(){return t.postForm(e,(0,r.default)(this).serialize()),!1}))}))},t.loadResponseText=function(e){var o=JSON.parse(e);t.loadBody(o)},t.loadBody=function(o){o.html&&(t.body.html(o.html),i.modal("show")),e.onload&&o.step&&o.step in e.onload&&e.onload[o.step](t,o)},t.respond=function(e){if(e in o){var n=Array.prototype.slice.call(arguments,1);o[e].apply(t,n)}},t.close=function(){i.modal("hide")},t.loadUrl(e.url,e.urlParams),t}},5311:e=>{e.exports=jQuery}},o={};function n(e){var r=o[e];if(void 0!==r)return r.exports;var a=o[e]={exports:{}};return t[e].call(a.exports,a,a.exports,n),a.exports}n.m=t,e=[],n.O=(t,o,r,a)=>{if(!o){var i=1/0;for(u=0;u<e.length;u++){for(var[o,r,a]=e[u],l=!0,d=0;d<o.length;d++)(!1&a||i>=a)&&Object.keys(n.O).every((e=>n.O[e](o[d])))?o.splice(d--,1):(l=!1,a<i&&(i=a));if(l){e.splice(u--,1);var s=r();void 0!==s&&(t=s)}}return t}a=a||0;for(var u=e.length;u>0&&e[u-1][2]>a;u--)e[u]=e[u-1];e[u]=[o,r,a]},n.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return n.d(t,{a:t}),t},n.d=(e,t)=>{for(var o in t)n.o(t,o)&&!n.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})},n.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),n.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),n.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.j=6922,(()=>{var e={6922:0};n.O.j=t=>0===e[t];var t=(t,o)=>{var r,a,[i,l,d]=o,s=0;if(i.some((t=>0!==e[t]))){for(r in l)n.o(l,r)&&(n.m[r]=l[r]);if(d)var u=d(n)}for(t&&t(o);s<i.length;s++)a=i[s],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(u)},o=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))})();var r=n.O(void 0,[2751],(()=>n(533)));r=n.O(r)})();