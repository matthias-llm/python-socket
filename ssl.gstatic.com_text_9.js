(function(){try{var i=void 0,k=!0,l=null,m=!1,r,s=this,t=function(a,b){var c=a.split("."),e=s;!(c[0]in e)&&e.execScript&&e.execScript("var "+c[0]);for(var f;c.length&&(f=c.shift());)!c.length&&b!==i?e[f]=b:e=e[f]?e[f]:e[f]={}},aa=function(a){for(var a=a.split("."),b=s,c;c=a.shift();)if(b[c]!=l)b=b[c];else return l;return b},ba=function(){},ca=function(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==
c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";else if("function"==b&&"undefined"==typeof a.call)return"object";return b},u=function(a){return"array"==ca(a)},w=function(a){return"string"==typeof a},
x=function(a){return"function"==ca(a)},y=function(a){return a[da]||(a[da]=++ea)},da="closure_uid_"+Math.floor(2147483648*Math.random()).toString(36),ea=0,fa=function(a,b,c){return a.call.apply(a.bind,arguments)},ga=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var e=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,e);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},z=function(a,b,
c){z=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?fa:ga;return z.apply(l,arguments)},A=Date.now||function(){return+new Date},B=function(a,b){function c(){}c.prototype=b.prototype;a.v=b.prototype;a.prototype=new c};window.gbar.tev&&window.gbar.tev(3,"pw");var C=function(a){Error.captureStackTrace?Error.captureStackTrace(this,C):this.stack=Error().stack||"";a&&(this.message=""+a)};B(C,Error);var ha=/&/g,ia=/</g,ja=/>/g,ka=/\"/g,la=/[&<>\"]/;var ma=function(a){return a};var D=Array.prototype,na=D.indexOf?function(a,b,c){return D.indexOf.call(a,b,c)}:function(a,b,c){c=c==l?0:0>c?Math.max(0,a.length+c):c;if(w(a))return!w(b)||1!=b.length?-1:a.indexOf(b,c);for(;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},oa=D.forEach?function(a,b,c){D.forEach.call(a,b,c)}:function(a,b,c){for(var e=a.length,f=w(a)?a.split(""):a,d=0;d<e;d++)d in f&&b.call(c,f[d],d,a)},pa=D.filter?function(a,b,c){return D.filter.call(a,b,c)}:function(a,b,c){for(var e=a.length,f=[],d=0,g=w(a)?
a.split(""):a,h=0;h<e;h++)if(h in g){var j=g[h];b.call(c,j,h,a)&&(f[d++]=j)}return f},qa=D.some?function(a,b,c){return D.some.call(a,b,c)}:function(a,b,c){for(var e=a.length,f=w(a)?a.split(""):a,d=0;d<e;d++)if(d in f&&b.call(c,f[d],d,a))return k;return m},E=function(a,b){return 0<=na(a,b)},ra=function(a,b,c){return 2>=arguments.length?D.slice.call(a,b):D.slice.call(a,b,c)};var sa=function(a){var b=F,c;for(c in b)a.call(i,b[c],c,b)},ta=function(a){var b=ca(a);if("object"==b||"array"==b){if(a.ib)return a.ib();var b="array"==b?[]:{},c;for(c in a)b[c]=ta(a[c]);return b}return a},ua="constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(","),va=function(a,b){for(var c,e,f=1;f<arguments.length;f++){e=arguments[f];for(c in e)a[c]=e[c];for(var d=0;d<ua.length;d++)c=ua[d],Object.prototype.hasOwnProperty.call(e,c)&&(a[c]=e[c])}};var G,wa,xa,ya,za=function(){return s.navigator?s.navigator.userAgent:l};ya=xa=wa=G=m;var Aa;if(Aa=za()){var Ba=s.navigator;G=0==Aa.indexOf("Opera");wa=!G&&-1!=Aa.indexOf("MSIE");xa=!G&&-1!=Aa.indexOf("WebKit");ya=!G&&!xa&&"Gecko"==Ba.product}var Ca=G,H=wa,I=ya,J=xa,Da;
a:{var Ea="",K;if(Ca&&s.opera)var Fa=s.opera.version,Ea="function"==typeof Fa?Fa():Fa;else if(I?K=/rv\:([^\);]+)(\)|;)/:H?K=/MSIE\s+([^\);]+)(\)|;)/:J&&(K=/WebKit\/(\S+)/),K)var Ga=K.exec(za()),Ea=Ga?Ga[1]:"";if(H){var Ha,Ia=s.document;Ha=Ia?Ia.documentMode:i;if(Ha>parseFloat(Ea)){Da=""+Ha;break a}}Da=Ea}
var Ja=Da,Ka={},L=function(a){var b;if(!(b=Ka[a])){b=0;for(var c=(""+Ja).replace(/^[\s\xa0]+|[\s\xa0]+$/g,"").split("."),e=(""+a).replace(/^[\s\xa0]+|[\s\xa0]+$/g,"").split("."),f=Math.max(c.length,e.length),d=0;0==b&&d<f;d++){var g=c[d]||"",h=e[d]||"",j=RegExp("(\\d*)(\\D*)","g"),n=RegExp("(\\d*)(\\D*)","g");do{var p=j.exec(g)||["","",""],o=n.exec(h)||["","",""];if(0==p[0].length&&0==o[0].length)break;b=((0==p[1].length?0:parseInt(p[1],10))<(0==o[1].length?0:parseInt(o[1],10))?-1:(0==p[1].length?
0:parseInt(p[1],10))>(0==o[1].length?0:parseInt(o[1],10))?1:0)||((0==p[2].length)<(0==o[2].length)?-1:(0==p[2].length)>(0==o[2].length)?1:0)||(p[2]<o[2]?-1:p[2]>o[2]?1:0)}while(0==b)}b=Ka[a]=0<=b}return b},La={},Ma=function(){return La[9]||(La[9]=H&&!!document.documentMode&&9<=document.documentMode)};var Na=function(a){Na[" "](a);return a};Na[" "]=ba;!H||Ma();var Oa=!H||Ma(),Pa=H&&!L("8");!J||L("528");I&&L("1.9b")||H&&L("8")||Ca&&L("9.5")||J&&L("528");I&&!L("8")||H&&L("9");var M=function(){};M.prototype.Ia=m;M.prototype.W=function(){this.Ia||(this.Ia=k,this.d())};M.prototype.d=function(){this.gb&&Qa.apply(l,this.gb);if(this.Ka)for(;this.Ka.length;)this.Ka.shift()()};var Ra=function(a){a&&"function"==typeof a.W&&a.W()},Qa=function(a){for(var b=0,c=arguments.length;b<c;++b){var e=arguments[b],f=e,d=ca(f);"array"==d||"object"==d&&"number"==typeof f.length?Qa.apply(l,e):Ra(e)}};var N=function(a,b){this.type=a;this.currentTarget=this.target=b};B(N,M);r=N.prototype;r.d=function(){delete this.type;delete this.target;delete this.currentTarget};r.t=m;r.defaultPrevented=m;r.T=k;r.preventDefault=function(){this.defaultPrevented=k;this.T=m};var O=function(a,b){a&&this.init(a,b)};B(O,N);r=O.prototype;r.target=l;r.relatedTarget=l;r.offsetX=0;r.offsetY=0;r.clientX=0;r.clientY=0;r.screenX=0;r.screenY=0;r.button=0;r.keyCode=0;r.charCode=0;r.ctrlKey=m;r.altKey=m;r.shiftKey=m;r.metaKey=m;r.ha=l;
r.init=function(a,b){var c=this.type=a.type;N.call(this,c);this.target=a.target||a.srcElement;this.currentTarget=b;var e=a.relatedTarget;if(e){if(I){var f;a:{try{Na(e.nodeName);f=k;break a}catch(d){}f=m}f||(e=l)}}else"mouseover"==c?e=a.fromElement:"mouseout"==c&&(e=a.toElement);this.relatedTarget=e;this.offsetX=J||a.offsetX!==i?a.offsetX:a.layerX;this.offsetY=J||a.offsetY!==i?a.offsetY:a.layerY;this.clientX=a.clientX!==i?a.clientX:a.pageX;this.clientY=a.clientY!==i?a.clientY:a.pageY;this.screenX=
a.screenX||0;this.screenY=a.screenY||0;this.button=a.button;this.keyCode=a.keyCode||0;this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.state=a.state;this.ha=a;a.defaultPrevented&&this.preventDefault();delete this.t};
r.preventDefault=function(){O.v.preventDefault.call(this);var a=this.ha;if(a.preventDefault)a.preventDefault();else if(a.returnValue=m,Pa)try{if(a.ctrlKey||112<=a.keyCode&&123>=a.keyCode)a.keyCode=-1}catch(b){}};r.d=function(){O.v.d.call(this);this.relatedTarget=this.currentTarget=this.target=this.ha=l};var Sa=function(){},Ta=0;r=Sa.prototype;r.key=0;r.s=m;r.Ha=m;r.init=function(a,b,c,e,f,d){if(x(a))this.Ga=k;else if(a&&a.handleEvent&&x(a.handleEvent))this.Ga=m;else throw Error("Invalid listener argument");this.C=a;this.xa=b;this.src=c;this.type=e;this.capture=!!f;this.ca=d;this.Ha=m;this.key=++Ta;this.s=m};r.handleEvent=function(a){return this.Ga?this.C.call(this.ca||this.src,a):this.C.handleEvent.call(this.C,a)};var P={},Q={},F={},R={},Ua=function(a,b,c,e,f){if(b){if(u(b)){for(var d=0;d<b.length;d++)Ua(a,b[d],c,e,f);return l}var e=!!e,g=Q;b in g||(g[b]={e:0,c:0});g=g[b];e in g||(g[e]={e:0,c:0},g.e++);var g=g[e],h=y(a),j;g.c++;if(g[h]){j=g[h];for(d=0;d<j.length;d++)if(g=j[d],g.C==c&&g.ca==f){if(g.s)break;return j[d].key}}else j=g[h]=[],g.e++;d=Va();d.src=a;g=new Sa;g.init(c,d,a,b,e,f);c=g.key;d.key=c;j.push(g);P[c]=g;F[h]||(F[h]=[]);F[h].push(g);a.addEventListener?(a==s||!a.ya)&&a.addEventListener(b,d,e):
a.attachEvent(b in R?R[b]:R[b]="on"+b,d);return c}throw Error("Invalid event type");},Va=function(){var a=Wa,b=Oa?function(c){return a.call(b.src,b.key,c)}:function(c){c=a.call(b.src,b.key,c);if(!c)return c};return b},Xa=function(a,b,c,e,f){if(u(b))for(var d=0;d<b.length;d++)Xa(a,b[d],c,e,f);else{e=!!e;a:{d=Q;if(b in d&&(d=d[b],e in d&&(d=d[e],a=y(a),d[a]))){a=d[a];break a}a=l}if(a)for(d=0;d<a.length;d++)if(a[d].C==c&&a[d].capture==e&&a[d].ca==f){Ya(a[d].key);break}}},Ya=function(a){if(!P[a])return m;
var b=P[a];if(b.s)return m;var c=b.src,e=b.type,f=b.xa,d=b.capture;c.removeEventListener?(c==s||!c.ya)&&c.removeEventListener(e,f,d):c.detachEvent&&c.detachEvent(e in R?R[e]:R[e]="on"+e,f);c=y(c);if(F[c]){var f=F[c],g=na(f,b);0<=g&&D.splice.call(f,g,1);0==f.length&&delete F[c]}b.s=k;if(b=Q[e][d][c])b.Da=k,Za(e,d,c,b);delete P[a];return k},Za=function(a,b,c,e){if(!e.S&&e.Da){for(var f=0,d=0;f<e.length;f++)e[f].s?e[f].xa.src=l:(f!=d&&(e[d]=e[f]),d++);e.length=d;e.Da=m;0==d&&(delete Q[a][b][c],Q[a][b].e--,
0==Q[a][b].e&&(delete Q[a][b],Q[a].e--),0==Q[a].e&&delete Q[a])}},$a=function(a){var b,c=0,e=b==l;b=!!b;if(a==l)sa(function(a){for(var d=a.length-1;0<=d;d--){var f=a[d];if(e||b==f.capture)Ya(f.key),c++}});else if(a=y(a),F[a])for(var a=F[a],f=a.length-1;0<=f;f--){var d=a[f];if(e||b==d.capture)Ya(d.key),c++}},bb=function(a,b,c,e,f){var d=1,b=y(b);if(a[b]){a.c--;a=a[b];a.S?a.S++:a.S=1;try{for(var g=a.length,h=0;h<g;h++){var j=a[h];j&&!j.s&&(d&=ab(j,f)!==m)}}finally{a.S--,Za(c,e,b,a)}}return Boolean(d)},
ab=function(a,b){a.Ha&&Ya(a.key);return a.handleEvent(b)},Wa=function(a,b){if(!P[a])return k;var c=P[a],e=c.type,f=Q;if(!(e in f))return k;var f=f[e],d,g;if(!Oa){d=b||aa("window.event");var h=k in f,j=m in f;if(h){if(0>d.keyCode||d.returnValue!=i)return k;a:{var n=m;if(0==d.keyCode)try{d.keyCode=-1;break a}catch(p){n=k}if(n||d.returnValue==i)d.returnValue=k}}n=new O;n.init(d,this);d=k;try{if(h){for(var o=[],q=n.currentTarget;q;q=q.parentNode)o.push(q);g=f[k];g.c=g.e;for(var v=o.length-1;!n.t&&0<=
v&&g.c;v--)n.currentTarget=o[v],d&=bb(g,o[v],e,k,n);if(j){g=f[m];g.c=g.e;for(v=0;!n.t&&v<o.length&&g.c;v++)n.currentTarget=o[v],d&=bb(g,o[v],e,m,n)}}else d=ab(c,n)}finally{o&&(o.length=0),n.W()}return d}e=new O(b,this);try{d=ab(c,e)}finally{e.W()}return d};var S=function(a){this.g=a};S.prototype.ka=function(a){return a};S.prototype.la=function(a){return a};S.prototype.V=0;S.prototype.update=function(a,b){var c=T(this.g,a);!b||b.error||!b.result?cb(c,l,this.V):db(c,b.result,this.V)};var eb=function(a){this.g=a};B(eb,S);eb.prototype.ka=function(a){var b=a.params,c=b&&b.optimistic,e=b&&b.id;this.U=e;var f=T(this.g,e).get(),f=f?ta(f):{id:e,isSetByViewer:m,metadata:{}},d;d=f||{};d.metadata=d.metadata||{};d.metadata.globalCounts=d.metadata.globalCounts||{};this.Fa(f,b);this.Va=f;c&&(cb(T(this.g,e),f),a=ta(a),delete a.params.optimistic);this.V=T(this.g,e).u;return a};
eb.prototype.la=function(a){if(a.result){var b=a.result,c=this.Va;b.metadata=b.metadata||c.metadata;b.metadata.globalCounts=b.metadata.globalCounts||c.metadata.globalCounts;b.metadata.globalCounts.count=b.metadata.globalCounts.count||c.metadata.globalCounts.count;if(c=b.metadata.globalCounts.person||c.metadata.globalCounts.person)b.metadata.globalCounts.person=c}this.update(this.U,a);return a};var fb=function(a){this.g=a};B(fb,eb);fb.prototype.Fa=function(a){a.isSetByViewer&&a.metadata.globalCounts.count!=i&&(a.metadata.globalCounts.count=Math.max(a.metadata.globalCounts.count-1,0));a.isSetByViewer=m};var gb=function(a){this.g=a};B(gb,S);gb.prototype.ka=function(a){this.U=a.params&&a.params.id;this.V=T(this.g,this.U).u;return a};gb.prototype.la=function(a){this.update(this.U,a);return a};var hb=function(a){this.g=a};B(hb,eb);hb.prototype.Fa=function(a,b){!a.isSetByViewer&&a.metadata.globalCounts.count!=i&&a.metadata.globalCounts.count++;a.isSetByViewer=k;a.aclJson=b.aclJson};var ib=function(){};B(ib,M);r=ib.prototype;r.ya=k;r.da=l;r.addEventListener=function(a,b,c,e){Ua(this,a,b,c,e)};r.removeEventListener=function(a,b,c,e){Xa(this,a,b,c,e)};
r.dispatchEvent=function(a){var b=a.type||a,c=Q;if(b in c){if(w(a))a=new N(a,this);else if(a instanceof N)a.target=a.target||this;else{var e=a,a=new N(b,this);va(a,e)}var e=1,f,c=c[b],b=k in c,d;if(b){f=[];for(d=this;d;d=d.da)f.push(d);d=c[k];d.c=d.e;for(var g=f.length-1;!a.t&&0<=g&&d.c;g--)a.currentTarget=f[g],e&=bb(d,f[g],a.type,k,a)&&a.T!=m}if(m in c)if(d=c[m],d.c=d.e,b)for(g=0;!a.t&&g<f.length&&d.c;g++)a.currentTarget=f[g],e&=bb(d,f[g],a.type,m,a)&&a.T!=m;else for(f=this;!a.t&&f&&d.c;f=f.da)a.currentTarget=
f,e&=bb(d,f,a.type,m,a)&&a.T!=m;a=Boolean(e)}else a=k;return a};r.d=function(){ib.v.d.call(this);$a(this);this.da=l};var jb=function(a,b){this.ma=a||l;this.r=b||l;this.u=1};B(jb,ib);jb.prototype.get=function(){return this.r||this.ma};var cb=function(a,b,c){if(!c||c==a.u)a.r=b,a.u++,a.dispatchEvent("change")},db=function(a,b,c){!c||c==a.u?(a.r=l,a.u++,a.ma=b,a.dispatchEvent("change")):(a.ma=b,a.r||a.dispatchEvent("change"))};var kb=function(){this.B=[]};kb.prototype.A=0;var lb=function(a,b){if(!(1<=a.A))return b(),0;return!(1<=a.B.length)?(a.B.push(b),1):2};var U=function(a){this.oa={};this.pa={};this.na=(a||window.googleapis).plusones};U.prototype.get=function(a){return mb(this,this.na.get(a))};U.prototype.insert=function(a){return mb(this,this.na.insert(a))};U.prototype.remove=function(a){return mb(this,this.na.remove(a))};var T=function(a,b){a.oa[b]||(a.oa[b]=new jb);return a.oa[b]},nb=function(a,b){a.pa[b]||(a.pa[b]=new kb);return a.pa[b]};
U.prototype.ua=function(a,b){var c=a.id;return ma(Ua(T(this,c),"change",z(function(){var a=T(this,c);b(a.get(),!a.r)},this)))};var mb=function(a,b){b.transport={name:"wrapped_googleapis",execute:z(a.jb,a,b.transport)};return b};
U.prototype.jb=function(a,b,c){for(var e={},f=[],d=[],g=0,h=b.length;g<h;++g){var j=b[g],n=ob(this,j);n&&(n.A++,d.push(n));n=j.id;e[n]=pb(this,j);(j=e[n].ka(j))&&f.push(j)}a.execute(f,z(function(a){for(var b=0,f=d.length;b<f;++b){var g=d[b];for(g.A--;!(1<=g.A)&&g.B.length;)g.B.shift()()}var b={},h;for(h in e)(f=e[h].la(a[h]||l))&&(b[h]=f);c(b)},this))};
var pb=function(a,b){switch(b.method){case "pos.plusones.get":return new gb(a);case "pos.plusones.insert":return new hb(a);case "pos.plusones.delete":return new fb(a);default:return new S(a)}},ob=function(a,b){var c=b.method,e=b.params,e=e&&e.id;return("pos.plusones.insert"==c||"pos.plusones.delete"==c)&&e?nb(a,e):l};var qb=function(a,b){b||(b={});var c=window,e="undefined"!=typeof a.href?a.href:""+a,f=b.target||a.target,d=[],g;for(g in b)switch(g){case "width":case "height":case "top":case "left":d.push(g+"="+b[g]);break;case "target":case "noreferrer":break;default:d.push(g+"="+(b[g]?1:0))}d=d.join(",");if(b.noreferrer){if(c=c.open("",f,d))H&&-1!=e.indexOf(";")&&(e="'"+e.replace(/'/g,"%27")+"'"),c.opener=l,J?c.location.href=e:(la.test(e)&&(-1!=e.indexOf("&")&&(e=e.replace(ha,"&amp;")),-1!=e.indexOf("<")&&(e=
e.replace(ia,"&lt;")),-1!=e.indexOf(">")&&(e=e.replace(ja,"&gt;")),-1!=e.indexOf('"')&&(e=e.replace(ka,"&quot;"))),c.document.write('<META HTTP-EQUIV="refresh" content="0; url='+e+'">'),c.document.close())}else c=c.open(e,f,d);return c};/*
 Portions of this code are from MochiKit, received by
 The Closure Authors under the MIT license. All other code is Copyright
 2005-2009 The Closure Authors. All Rights Reserved.
*/
var rb=function(a,b){this.R=[];this.Na=b||l};r=rb.prototype;r.D=m;r.F=m;r.G=0;r.Ja=m;r.Pa=m;r.Oa=0;r.Aa=function(a,b){sb(this,a,b);this.G--;0==this.G&&this.D&&tb(this)};var sb=function(a,b,c){a.D=k;a.fa=c;a.F=!b;tb(a)},vb=function(a){if(a.D){if(!a.Ja)throw new ub;a.Ja=m}};rb.prototype.addCallback=function(a,b){return wb(this,a,l,b)};
var wb=function(a,b,c,e){a.R.push([b,c,e]);a.D&&tb(a);return a},xb=function(a){return qa(a.R,function(a){return x(a[1])})},tb=function(a){a.ga&&a.D&&xb(a)&&(s.clearTimeout(a.ga),delete a.ga);a.Ba&&(a.Ba.Oa--,delete a.Ba);for(var b=a.fa,c=m,e=m;a.R.length&&0==a.G;){var f=a.R.shift(),d=f[0],g=f[1],f=f[2];if(d=a.F?g:d)try{var h=d.call(f||a.Na,b);h!==i&&(a.F=a.F&&(h==b||h instanceof Error),a.fa=b=h);b instanceof rb&&(e=k,a.G++)}catch(j){b=j,a.F=k,xb(a)||(c=k)}}a.fa=b;e&&a.G&&(wb(b,z(a.Aa,a,k),z(a.Aa,
a,m)),b.Pa=k);c&&(a.ga=s.setTimeout(function(){throw new yb(b);},0))},ub=function(){C.call(this)};B(ub,C);ub.prototype.message="Already called";var yb=function(a){C.call(this);this.message="Unhandled Error in Deferred: "+(a.message||"[No message]")};B(yb,C);var zb=function(){};var Ab=function(){this.ia={}};Ab.prototype.setData=function(a){this.ia=Object(a)};Ab.prototype.ea=function(){return""+(this.ia.version||"")};var Bb=function(a,b,c,e){a=a||window;"number"!=typeof c&&(c=800);"number"!=typeof e&&(e=600);var f=a.outerHeight!=l?a.outerHeight:a.document.documentElement.clientHeight,d=a.screenY!=l?a.screenY:a.screenTop,a=Math.max(0,(a.screenX!=l?a.screenX:a.screenLeft)+((a.outerWidth!=l?a.outerWidth:a.document.documentElement.clientWidth)>>1)-(c>>1)),f=Math.max(0,d+(f>>1)-(e>>1)),c={left:a,top:f,menubar:m,toolbar:m,location:m,status:k,scrollbars:k,width:c,height:e};b&&(c.target=b);return c};var Db=function(a,b){this.Ra=a;this.Ta="GooglePlusPopupSignup";this.X="https://plus.google.com";this.Sa=""+Math.floor(1E9*Math.random());this.ra=Cb();this.za=l;this.L=new rb;this.Qa=b;this.Ca=[1100,850];this.qa=m};B(Db,zb);var Cb=function(){var a=window;return a.location.protocol+"//"+a.location.host};r=Db.prototype;r.w=m;r.aa=l;r.ea=function(){return this.Wa};
r.show=function(a){var b=this.X+"/_/+1/messageproxy";if(!this.Ea){var c=document.createElement("div");c.style.position="absolute";c.style.left="-1000px";c.style.top="-1000px";c.style.width="1px";c.style.height="1px";document.body.appendChild(c);this.Ea=iframes.open(b,{container:c},{},{handleMessage:z(this.Ua,this)})}b=this.X+"/+1/profile/?type=po&client="+this.Qa+"&gpsrc="+encodeURIComponent(this.Ra)+"&parent="+encodeURIComponent(this.ra)+"&proxy="+this.Ea.getId();this.za&&(b+="&continue="+encodeURIComponent(this.za));
this.qa&&(b+="&rsz=1");b+=(!window.__P1_LOCALE?"":"&hl="+window.__P1_LOCALE)+"#"+this.Sa;(a=qb(b,Bb(a,this.Ta,this.Ca[0],this.Ca[1])))&&a.focus();return a};r.Ua=function(a){try{var b=new Ab;b.setData(a);this.w=!!b.ia.created;this.Wa=b.ea();var c=this.L;vb(c);sb(c,k,b)}catch(e){if(this.aa)try{this.aa(e)}catch(f){}a=this.L;vb(a);sb(a,m,e)}};!H||Ma();!I&&!H||H&&Ma()||I&&L("1.9.1");H&&L("9");var Eb=function(a){a=a.className;return w(a)&&a.match(/\S+/g)||[]},Gb=function(a,b){var c=Eb(a),e=ra(arguments,1);Fb(c,e);a.className=c.join(" ")},Fb=function(a,b){for(var c=0;c<b.length;c++)E(a,b[c])||a.push(b[c])},Hb=function(a,b){return pa(a,function(a){return!E(b,a)})};var Ib=function(a){var b=a||document;if(b.querySelectorAll&&b.querySelector)a=b.querySelectorAll(".esw");else if(b.getElementsByClassName)a=b.getElementsByClassName("esw");else{var c,e,a=a||document;if(a.querySelectorAll&&a.querySelector)a=a.querySelectorAll(".esw");else if(a.getElementsByClassName)var f=a.getElementsByClassName("esw"),a=f;else{f=a.getElementsByTagName("*");e={};for(b=c=0;a=f[b];b++){var d=a.className;"function"==typeof d.split&&E(d.split(/\s+/),"esw")&&(e[c++]=a)}e.length=c;a=e}}return a};var V=function(a){this.eb=a;this.ja=[]};B(V,M);var Jb=[];V.prototype.ua=function(a,b,c,e,f){u(b)||(Jb[0]=b,b=Jb);for(var d=0;d<b.length;d++)this.ja.push(Ua(a,b[d],c||this,e||m,f||this.eb||this));return this};V.prototype.d=function(){V.v.d.call(this);oa(this.ja,Ya);this.ja.length=0};V.prototype.handleEvent=function(){throw Error("EventHandler.handleEvent not implemented");};var Kb=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^/?#]*)@)?([\\w\\d\\-\\u0100-\\uffff.%]*)(?::([0-9]+))?)?([^?#]+)?(?:\\?([^#]*))?(?:#(.*))?$"),Mb=function(a){if(Lb){Lb=m;var b=s.location;if(b){var c=b.href;if(c&&(c=(c=Mb(c)[3]||l)&&decodeURIComponent(c))&&c!=b.hostname)throw Lb=k,Error();}}return a.match(Kb)},Lb=J,Nb=function(a,b,c){if(u(b))for(var e=0;e<b.length;e++)Nb(a,""+b[e],c);else b!=l&&c.push("&",a,""===b?"":"=",encodeURIComponent(""+b))};var Ob=function(a){this.$=a||"inline";this.H={z:ba,p:ba,error:ba}},Pb=function(a,b){x(b)&&(a.H.p=b,a.H.z=function(a){b({evt:a})})};var Qb=function(){this.h=Mb(window.location.href)};var Rb=function(a,b,c){this.title=a;this.thumbnailUrl=b;this.fb=c},W=function(a,b,c,e,f,d,g){V.call(this);this.a=a;this.Y=b;Gb(b,"esw");this.J=this.a.J;if(this.P=e||l)if((a=this.P.getElementsByTagName("a"))&&a[0])a[0].onclick=z(function(){Sb(this,m);lb(nb(this.a.o,this.n),z(this.sa,this,A()-this.J));window.event&&(window.event.returnValue=m);return m},this);E(Eb(b),"eswa")||Gb(b,"eswd");this.f=this.a.H;this.ta=f?f.split(" "):[];this.n=c;this.$=d||l;this.O=g||l;this.k=T(this.a.o,c);this.ua(this.k,
"change",this.K)};B(W,V);var Tb={qb:"eswa",pb:"eswd",ob:"eswh",rb:"esww",nb:"eswe"};W.prototype.M=m;W.prototype.ba=m;W.prototype.wa=function(a){if(a&&a.error&&a.error.code){this.M=k;switch(a.error.code){case 401:this.a.I.w=m}this.f.error({code:a.error.code,message:a.error.message,entity:this.n});this.K()}else a&&this.f.p({resp:"plusone",state:a.isSetByViewer})};
W.prototype.toggle=function(){var a=this.k.get(),a=!!a&&a.isSetByViewer;this.f.z("click");var b;b=this.a.I;b.w?this.M?(qb("https://www.google.com/support/profiles/?p=plusone_button_error&hl=en",Bb(window,"GooglePlusOneHelp",800,600)),this.f.z("help_window"),b=k):b=m:(b.L.addCallback(this.La,this),b.show(window),this.ba=!!a,this.f.p({req:"signup"}),b=k);b||(Ub(this)?this.f.z("blocked"):Vb(this,a))};
var Vb=function(a,b){var c=window.google||l;c&&(c.comm&&c.comm.j&&c.comm.j(),c.j&&c.j.cl&&c.j.cl());c=b?a.sa:a.Ma;Sb(a,!b);c=lb(nb(a.a.o,a.n),z(c,a,A()-a.J));b&&2!=c?window.setTimeout(z(a.K,a),150):2==c&&a.f.z("throttler_rejected")},Wb=function(a,b,c){a={id:a.n,cdx:b.toString(16),gpsrc:"inline",source:a.$||a.a.$};c&&(a.optimistic=k);return a};
W.prototype.Ma=function(a){var b=this.k.get();if(!b||!b.isSetByViewer)this.f.p({req:"plusone",evt:"set_plusone"}),this.a.o.insert(Xb(this,Yb(this,Wb(this,a,k)))).execute(z(this.wa,this));$b(this,k)};W.prototype.sa=function(a){var b=this.k.get();b&&b.isSetByViewer&&(this.f.p({req:"plusone",evt:"set_unplusone"}),this.a.o.remove(Xb(this,Wb(this,a,m))).execute(z(this.wa,this)));$b(this,m)};
var Yb=function(a,b){a.O&&(b.image_title=a.O.title,b.image_thumbnail=a.O.thumbnailUrl,b.image_landing=a.O.fb);return b},Xb=function(a,b){var c=a.a.I.ea();c&&(b.profileVersion=c);return b},Sb=function(a,b){a.P&&(a.P.style.display=b?"":"none")},$b=function(a,b){for(var c=new Qb,e=0,f=a.ta.length;e<f;++e){var d=a.ta[e];if(d){var g=c,d=Mb(d),h=d[1];h||(d[1]=g.h[1],h=d[2]);h||(d[2]=g.h[2],h=d[3]);h||(d[3]=g.h[3],h=d[4]);if(!h){d[4]=g.h[4];var j=d[5],n=g.h[5];if(h=j){if("/"!=j.charAt(0))if(g.h[3]&&!n)j=
"/"+j;else{var p=n.lastIndexOf("/");-1!=p&&(j=n.substr(0,p+1)+j)}n=d;if(".."==j||"."==j)p="";else if(-1==j.indexOf("./")&&-1==j.indexOf("/."))p=j;else{for(var p=0==j.lastIndexOf("/",0),j=j.split("/"),o=[],q=0;q<j.length;){var v=j[q++];"."==v?p&&q==j.length&&o.push(""):".."==v?((1<o.length||1==o.length&&""!=o[0])&&o.pop(),p&&q==j.length&&o.push("")):(o.push(v),p=k)}p=o.join("/")}n[5]=p}}h||(d[5]=g.h[5],h=d[6]);h||(d[6]=g.h[6],h=d[7]);h||(d[7]=g.h[7]);g=d[1];h=d[2];n=d[3];p=d[4];j=d[5];o=d[6];d=d[7];
q=[];g&&q.push(g,":");n&&(q.push("//"),h&&q.push(h,"@"),q.push(n),p&&q.push(":",p));j&&q.push(j);o&&q.push("?",o);d&&q.push("#",d);d=q.join("");if(0==d.lastIndexOf("http://",0)||0==d.lastIndexOf("https://",0)){g={entity:a.n,toggle:b?"on":"off"};window.google&&window.google.kEI&&(g.ei=window.google.kEI);g.zx=Math.floor(2147483648*Math.random()).toString(36)+Math.abs(Math.floor(2147483648*Math.random())^A()).toString(36);d=[d];h=i;for(h in g)Nb(h,g[h],d);d[1]&&(g=d[0],h=g.indexOf("#"),0<=h&&(d.push(g.substr(h)),
d[0]=g=g.substr(0,h)),h=g.indexOf("?"),0>h?d[1]="?":h==g.length-1&&(d[1]=i));d=d.join("");(new Image).src=d}}}};W.prototype.K=function(){try{if(this.Q){var a=this.Q-A();if(0<a){window.setTimeout(z(this.K,this),a);return}this.Q=i}if(this.M)ac(this,"eswe"),Sb(this,m);else{var b=this.k.get();b&&(Ub(this)?(ac(this,"esww"),this.Q=A()+650):ac(this,b.isSetByViewer?"eswa":"eswd"))}}catch(c){this.a.kb.log(c)}};
var ac=function(a,b){var c=[],e;for(e in Tb){var f=Tb[e];b!=f&&c.push(f)}e=a.Y;f=Eb(e);if(w(c)){var d=f,c=na(d,c);0<=c&&D.splice.call(d,c,1)}else u(c)&&(f=Hb(f,c));w(b)&&!E(f,b)?f.push(b):u(b)&&Fb(f,b);e.className=f.join(" ")},Ub=function(a){var b=nb(a.a.o,a.n);return!!a.Q||!!b.B.length||!!b.A&&!a.k.r};W.prototype.La=function(){var a=this.a.I,b=a.w;this.f.p({req:"signup",success:b});b&&(this.M=m,Vb(this,this.ba));this.ba=m;a.L=new rb};W.prototype.d=function(){W.v.d.call(this)};var X=function(a,b,c){a=a||{};this.b={};this.N=[];this.a=new Ob(c);this.a.Z=b||window.document;this.a.o=new U(a.googleapis);c=!!a.signed;b=new Db("g",1);b.aa=a.elog;b.qa=k;b.ra=Cb();b.w=c;if(c=a.base)c.match(/.*\/$/)&&(c=c.substr(0,c.length-1)),b.X=c;this.a.I=b;Pb(this.a,a.logEvent);b=this.a;c=a.logErr;x(c)&&(b.H.error=c);b=this.a;c=a.loadTime||A();b.J=c;this.va=a.logRender||l;bc(this)},cc;B(X,M);var dc=0;
t("gbar.pw.init",function(a,b,c){if(cc)throw Error("Registry already initialized");a=new X(a,b,c);b=z(a.bb,a);t("gbar.pw.clk",b);b=z(a.cb,a);t("gbar.pw.hvr",b);cc=a;if(a.va)try{a.va()}catch(e){}return a});t("gbar.pw.dsp",function(){Ra(cc);cc=l});
var bc=function(a){var b=Ib(a.a.Z),c={};oa(b,function(a){a.id||(a.id="gbpwm_"+dc++);var b=a.id;if(b in this.b)c[b]=this.b[b],delete this.b[b];else if(a=ec(this,a))c[b]&&this.N.push(c[b]),c[b]=a},a);fc(a);a.b=c},ec=function(a,b){var c=b.getAttribute("g:entity");if(!c)return l;var e=b.getAttribute("g:undo"),f=i;e&&(f=a.a.Z.getElementById(e));var e=b.getAttribute("g:pingback"),d=b.getAttribute("g:source"),g=b.getAttribute("g:imgtitle"),h=b.getAttribute("g:imgtbn"),j=b.getAttribute("g:imgland"),n=l;g&&
h&&j&&(n=new Rb(g,h,j));c=new W(a.a,b,c,f,e,d,n);f=E(Eb(c.Y),"eswa");(e=c.k.get())?e.isSetByViewer=f:e={id:c.n,isSetByViewer:f,metadata:{}};db(c.k,e);return c};X.prototype.bb=function(a){gc(this,a);a.id&&(a=this.b[a.id])&&a.toggle()};X.prototype.cb=function(a){if(a){gc(this,a);for(var b in this.b);}};
var gc=function(a,b){if(!b.id||!(b.id in a.b))bc(a);else if(b.id&&b.id in a.b){for(var c=a.b[b.id].Y;c&&c.parentNode;)c=c.parentNode;c!=a.a.Z&&(Ra(a.b[b.id]),(c=ec(a,b))&&(a.b[b.id]=c))}},fc=function(a){for(var b in a.b)Ra(a.b[b]);a.b=l};X.prototype.d=function(){fc(this);for(var a=0;a<this.N.length;a++)Ra(this.N[a]);this.N=l;X.v.d.call(this)};var Y=window.gbar;var Z={Xa:1,mb:2,lb:3,Za:4,Ya:5,ab:6,$a:7,hb:8};var hc=[],ic=l,$=function(a,b){var c=l;b&&(c={m:b});Y.tev&&Y.tev(a,"pw",c)};t("gbar.mddn",function(){for(var a=[],b=0,c;c=hc[b];++b)a.push(c[0]);return a.join(",")});hc.push(["pw",{init:function(a){a.signed=a.signed[0];var b=aa("gbar.logger.il");b&&(a.logRender=a.logRender||z(b,l,15),a.logEvent=a.logEvent||z(b,l,16),a.logErr=a.logErr||z(b,l,19));aa("gbar.pw.init")(a)}}]);$(Z.hb);
(function(){$(Z.Za);var a,b;for(a=0;(b=Y.bnc[a])&&!("pw"==b[0]);++a);b&&!b[1].l&&(a=function(){for(var a=Y.mdc,e=Y.mdi||{},f=0,d;d=hc[f];++f){var g=d[0],h=a[g],j=e[g],n;if(n=h){if(j=!j){var p;a:{j=g;if(n=Y.mdd)try{if(!ic){ic={};var o=n.split(/;/);for(n=0;n<o.length;++n)ic[o[n]]=k}p=ic[j];break a}catch(q){Y.logger&&Y.logger.ml(q)}p=m}j=!p}n=j}if(n){$(Z.ab,g);try{d[1].init(h),e[g]=k}catch(v){Y.logger&&Y.logger.ml(v)}$(Z.$a,g)}}if(a=Y.qd.pw){Y.qd.pw=[];for(e=0;f=a[e];++e)try{f()}catch(Zb){Y.logger&&Y.logger.ml(Zb)}}b[1].l=
k;$(Z.Ya);a:{for(a=0;e=Y.bnc[a];++a)if((e[1].auto||"m"==e[0])&&!e[1].l){a=m;break a}a=k}a&&$(Z.Xa)},!b[1].libs||Y.agl&&Y.agl(b[1].libs)?a():b[1].i=a)})();}catch(e){window.gbar&&gbar.logger&&gbar.logger.ml(e,{"_sn":"pw.init","_mddn":(gbar.mddn?gbar.mddn():"0")});}})();