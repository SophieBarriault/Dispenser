/*jshint -W069*/

/**
 * Minified by jsDelivr using Terser v3.14.1.
 * Original file: /npm/js-cookie@2.2.1/src/js.cookie.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
!function(e){var n;if("function"==typeof define&&define.amd&&(define(e),n=!0),"object"==typeof exports&&(module.exports=e(),n=!0),!n){var t=window.Cookies,o=window.Cookies=e();o.noConflict=function(){return window.Cookies=t,o}}}(function(){function e(){for(var e=0,n={};e<arguments.length;e++){var t=arguments[e];for(var o in t)n[o]=t[o]}return n}function n(e){return e.replace(/(%[0-9A-Z]{2})+/g,decodeURIComponent)}return function t(o){function r(){}function i(n,t,i){if("undefined"!=typeof document){"number"==typeof(i=e({path:"/"},r.defaults,i)).expires&&(i.expires=new Date(1*new Date+864e5*i.expires)),i.expires=i.expires?i.expires.toUTCString():"";try{var c=JSON.stringify(t);/^[\{\[]/.test(c)&&(t=c)}catch(e){}t=o.write?o.write(t,n):encodeURIComponent(String(t)).replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g,decodeURIComponent),n=encodeURIComponent(String(n)).replace(/%(23|24|26|2B|5E|60|7C)/g,decodeURIComponent).replace(/[\(\)]/g,escape);var f="";for(var u in i)i[u]&&(f+="; "+u,!0!==i[u]&&(f+="="+i[u].split(";")[0]));return document.cookie=n+"="+t+f}}function c(e,t){if("undefined"!=typeof document){for(var r={},i=document.cookie?document.cookie.split("; "):[],c=0;c<i.length;c++){var f=i[c].split("="),u=f.slice(1).join("=");t||'"'!==u.charAt(0)||(u=u.slice(1,-1));try{var a=n(f[0]);if(u=(o.read||o)(u,a)||n(u),t)try{u=JSON.parse(u)}catch(e){}if(r[a]=u,e===a)break}catch(e){}}return e?r[e]:r}}return r.set=i,r.get=function(e){return c(e,!1)},r.getJSON=function(e){return c(e,!0)},r.remove=function(n,t){i(n,"",e(t,{expires:-1}))},r.defaults={},r.withConverter=t,r}(function(){})});

// via https://code.broker/en/tutorials/store-utm-and-other-tracking-links-url-parameters-in-a-cookie/

(function () {
    // Retrieve my current url parameters
    function getParameter(theParameter) {
        var params = window.location.search.substr(1).split('&');
        for (var i = 0; i < params.length; i++) {
            var p = params[i].split('=');
            if (p[0] == theParameter) {
                return decodeURIComponent(p[1]);
            }
        }
        return false;
    }

    try {
        var params = {
            source: getParameter('utm_source'),
            medium: getParameter('utm_medium'),
            campaign: getParameter('utm_campaign'),
            ref: getParameter('ref'),

            host: document.location.host,
            path: document.location.pathname,
            referrer: document.referrer
        };

        var fbclid = getParameter('fbclid');
        if(fbclid && !params.ref) params.ref = "facebook";

        // I retrieve data from my cookie (if it exists) and I create an object in JavaScript.
        var original = Cookies.get('cookie_utms') || "{}";
        var cookie = JSON.parse(original);

        var keys = Object.keys(params), k, v;
        for(var i=0; i<keys.length; i++) {
            k = keys[i];
            v = params[k];

            if(v && !cookie[k]) cookie[k] = v;
        }

        var toSet = JSON.stringify(cookie);
        if(toSet != original) {
            Cookies.set('cookie_utms', toSet, {
                domain: "roboflow.com",
                expires: 120
            });
        }

        if(params.source || params.ref) {
            var request = new XMLHttpRequest();
            request.open('POST', 'https://app.roboflow.com/query/link', true);
            request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
            request.send(JSON.stringify(params));
        }

    } catch(e) {
        // ignore
    }

}());
