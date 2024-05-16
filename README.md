<html lang="en"><head><style class="vjs-styles-defaults">
      .video-js {
        width: 300px;
        height: 150px;
      }

      .vjs-fluid {
        padding-top: 56.25%
      }
    </style>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

      <script type="text/javascript" async="" src="https://trinketsofcody.com/cody-widget.js"></script><script type="text/javascript" async="" src="//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js"></script><script type="text/javascript" async="" src="https://cdn.mxpnl.com/libs/mixpanel-js-wrapper.js"></script><script type="text/javascript" async="" src="https://static.hotjar.com/c/hotjar-3897705.js?sv=7"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-BLGQHYCV6F&amp;l=dataLayer&amp;cx=c"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-N4C8MF2"></script><script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({"userId":508788,"visitorType":"student","batch":{"id":158,"fullNameWithC":"AFR-1123 (C#22)","schoolLocation":{"id":1,"name":"ALX Africa"}},"curriculum":{"id":1,"name":"SE Foundations"}});

    window.gtm_user_custom_event = function (name, options) {
      if (typeof name === 'undefined') {
        return;
      }

      window.dataLayer.push({
        customEventOptions: typeof options !== 'undefined' ? options : {},
        event: name,
      });
    }
  </script>

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-N4C8MF2');</script>
  <!-- End Google Tag Manager -->


    <title>Project: 0x00. AirBnB clone - The console | ALX Africa Intranet</title>

      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="/assets/application_alx-07a9a090e6d07d0af02db348d532bcb0598f5c5b263781671a4ba861200e8922.css">
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <script src="/assets/application-4013a5403da5765fc4df54f925fc1e4391897907edd19da0062bb21512c02328.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon_alx.ico">
      <meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="LsAw9q1pLLXPeapmG3br2B1enzLsdIqtG5DMWYbRboitYEiXD-nv4_WHtzrWL0mdYUh43aex-_a6839D7pMNvg">

      <link rel="apple-touch-icon" href="/apple-touch-icon_alx.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

      <!-- intro.js for interactive onboarding -->

      <!-- React -->
      <script src="/packs/js/application-f24fb2f5a47e086ae0bc.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-87456da7.css">
  <script async="" src="https://script.hotjar.com/modules.e5979922753cf3b8b069.js" charset="utf-8"></script><script src="https://js.userpilot.io/sdk/version/1.490/app.js" async=""></script><style nonce="undefined">
iframe#userpilot-nps {
  width: 900px;
  right: 0px;
  margin: 0px auto;
  opacity: 1 !important;
}

/* NPS Mobile */
@media (max-width: 900px) {
  iframe#userpilot-nps {
      width: 100%;
  }
}

iframe#userpilot-resource-centre-frame {
  width: 0px;
  height: 0px;
}

div#userpilotContent[key=""]:not(.preview) {
  position: absolute;
  line-height: 18px;
  -webkit-transition: none;
  transition: none;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  z-index: 2147483638;
  pointer-events: none;
  outline: none !important;
  background: none !important;
  --sidebar-width: 0px;
  direction: ltr;
  display: block;
}

div#userpilotContent[key=""] * {
  -webkit-transition: none;
  transition: none;
  direction: ltr;
}

#userpilotContent[key=""] .conv-cont, #userpilotContent[key=""] .conv-backdrop-cont {
  z-index: 999999999;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  pointer-events: none;
  transition: opacity 0.1s, z-index 0s, visibility 0s;
}

#userpilotContent[key=""] .conv-cont, #userpilotContent[key=""] .conv-backdrop-cont {
  z-index: 999999999;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  pointer-events: none;
  transition: opacity 0.1s, z-index 0s, visibility 0s;
}

#userpilotContent[key=""] .userpilot .conv-cont {
  z-index: 2147483000;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  pointer-events: none;
}

#userpilotContent[key=""] .conv-cont {
  background: none;
}

#userpilotContent[key=""] .canv {
  position: absolute;
  top: 0;
  box-shadow: inset 0 0 0 0px #ffffff, inset 0 0 15px rgb(208, 208, 208);
  background: none !important;
  display: flex;
  border: 10000px solid rgba(255, 255, 255, .56);
  margin-left: -10000px;
  margin-top: -10000px;
  padding: 150px;
  opacity: 0;
  transition: opacity 0.6s;
  border-radius: 10006px
}

#userpilotContent[key=""] .userpilot .canv {
  position: fixed;
  top: 0;
  background: none;
  display: flex;
  border: 10000px solid rgba(255, 255, 255, .7);
  margin-left: -10000px;
  margin-top: -10000px;
  padding: 150px;
  opacity: 0;
  border-radius: 10006px
}

#userpilotContent[key=""] .canv.userpilot-canv-hidden {
  opacity: 0 !important
}

#userpilotContent[key=""] .userpilot-soft-focus .canv {
  border: none
}

#userpilotContent[key=""] .conv-cont[userpilot-hidden] .up-userpilot-mmx-part{
  pointer-events: none !important;
}

#userpilotContent[key=""] .up-userpilot-mmx-part {
  position: absolute;
  z-index: 1 !important;
  background: none;
}

#userpilotContent[key=""] [up-backdrop="0"] {
  background: none !important;
  border: none !important;
  box-shadow: none !important;
}

#userpilotContent[key=""] .conv-cont[backdrop-overlay="1"] .up-userpilot-mmx-part {
  width: 100% !important;
  height: 100% !important;
  top: 0px !important;
  left: 0px !important;
}

#userpilotContent[key=""] .conv-cont.allow-scroll .up-userpilot-mmx-part {
  pointer-events: none;
}

div#userpilotContent[key=""]>*, div#userpilotContent[key=""]>*:not(.userpilot-hotspot-container)>*:not(.userpilot-backdrop) {
  pointer-events: all;
}

#userpilotContent[key=""] .userpilot-mmx-cursor {
  position: fixed;
  width: 14px;
  -webkit-transition: all 1.5s;
  transition: all 1.5s;
  pointer-events: none
}
#userpilotContent[key=""] .userpilot-mmx-cursor * {
  pointer-events: none !important;
}
#userpilotContent[key=""] .up-t-pluse {
  position: absolute;
  width: 14px;
  height: 14px;
  border: none;
  border-radius: 100%;
  color: gainsboro;
  background: gainsboro
}
#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse {
  width: 10px;
  height: 10px;
  pointer-events: none !important;
}
#userpilotContent[key=""] .up-t-pluse:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: -3px;
  top: -3px;
  background-color: transparent;
  border-radius: 50%;
  border: 7px solid;
  border-color: inherit;
  -webkit-animation: userpilotActive 2s infinite linear;
  animation: userpilotActive 2s infinite linear
}
#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse:before {
  height: 18px;
  width: 18px;
  left: -4px;
  top: -4px;
  border: 0px;
  background: inherit;
  -webkit-animation: userpilot-tooltip-pulse 2s infinite linear;
  animation: userpilot-tooltip-pulse 2s infinite linear
}
@keyframes userpilotActive {
  0% {
    -webkit-transform: scale(.1);
    border-color: inherit;
    opacity: 1
  }

  30% {
    -webkit-transform: scale(1);
    border: 5px solid;
    border-color: inherit;
    opacity: 1
  }

  40% {
    -webkit-transform: scale(1.3);
    border: 0 solid;
    border-color: inherit
  }

  100% {
    border: 0 solid;
    border-color: inherit
  }
}

@-webkit-keyframes active {
  0% {
    -webkit-transform: scale(.1);
    border-color: inherit;
    opacity: 1
  }

  30% {
    -webkit-transform: scale(1);
    border: 5px solid;
    border-color: inherit;
    opacity: 1
  }

  40% {
    -webkit-transform: scale(1.3);
    border: 0 solid;
    border-color: inherit
  }

  100% {
    border: 0 solid;
    border-color: inherit
  }
}

#userpilotContent[key=""] .userpilot-ripple {
  position: absolute;
  pointer-events: none;
  width: 0px;
  height: 30px;
  border: none;
  border-radius: 100%;
  left: 50%;
  top: 50%;
}
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple {
  height: 18px;
  width: 18px;
  background-color: transparent !important;
}
#userpilotContent[key=""] .userpilot-ripple:before {
  position: absolute;
  content: "";
  height: 30px;
  width: 30px;
  left: 0px;
  top: 0px;
  background-color: transparent;
  border-radius: 50%;
  background: inherit;
  -webkit-animation: userpilotActive 2s infinite linear;
  animation: userpilotActive 2s infinite linear;
  border: 10px solid;
  border-color: inherit;
  box-sizing: border-box;
}
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple:before {
  height: 18px;
  width: 18px;
  left: -1px;
  top: -1px;
  -webkit-animation: userpilot-tooltip-pulse 2s infinite linear;
  animation: userpilot-tooltip-pulse 2s infinite linear;
}
@-webkit-keyframes userpilot-tooltip-pulse {
  0%,
  100% {
    -webkit-transform: scale(0.8);
    -ms-transform: scale(0.8);
    transform: scale(0.8);
    opacity: 0.2;
  }

  50% {
    -webkit-transform: scale(0.9);
    -ms-transform: scale(0.9);
    transform: scale(0.9);
    opacity: 0.3;
  }
}

@keyframes userpilot-tooltip-pulse {
  0%,
  100% {
    -webkit-transform: scale(0.8);
    -ms-transform: scale(0.8);
    transform: scale(0.8);
    opacity: 0.2;
  }

  50% {
    -webkit-transform: scale(0.9);
    -ms-transform: scale(0.9);
    transform: scale(0.9);
    opacity: 0.3;
  }
}

#userpilotContent[key=""] .userpilot-ripple:after {
  position: absolute;
  content: "";
  height: 10px;
  width: 10px;
  left: 10px;
  top: 10px;
  background-color: transparent;
  border-radius: 50%;
  background: inherit;
  -webkit-animation: userpilot_active_after 2s infinite linear;
  animation: userpilot_active_after 2s infinite linear;
  box-sizing: border-box;
  background: currentColor;
}
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple:after {
  height: 10px;
  width: 10px;
  left: 4px;
  top: 4px;
  animation: none;
}
@keyframes userpilot_active_after {
  0% {
    -webkit-transform: scale(.1);
    opacity: 1
  }

  20% {
    opacity: 1;
    -webkit-transform: scale(1)
  }

  100% {
    opacity: 0;
    -webkit-transform: scale(5)
  }
}

@keyframes userpilotActive {
  0% {
    -webkit-transform: scale(.1);
    opacity: 1;
    border-color: inherit;
  }

  20% {
    opacity: 1;
    -webkit-transform: scale(1.5);
    border-color: inherit;
  }

  30% {
    background: none;
    border: 0 solid;
    border-color: inherit;
    opacity: 0
  }

  100% {
    opacity: 0;
    -webkit-transform: scale(2.5);
    border-color: inherit;
  }
}


/* sonar animations */
#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="sonar"], 
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="sonar"] {
  background: none !important;
  animation: none;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="sonar"]::after, 
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="sonar"]::after {
  content: "";
  width: 9px;
  height: 9px;
  position: absolute;
  border-radius: 150px;
  animation: pulse-dot infinite 1.5s;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: currentColor;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="sonar"]::before,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="sonar"]::before {
  left: 0px;
  top: 0px;
  animation: pulse-ring infinite 1.5s;
  border-style: solid;
  border-width: 4px;
  padding: 5px;
  background: none !important;
}

/* morph animation */
#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="morph"],
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="morph"] {
  background: none !important;
  animation: none;
  height: 18px;
  width: 18px;
  left: -4px;
  top: -4px;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="morph"]::before,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="morph"]::before {
  left: 0;
  top: 0;
  content: "";
  width: 100%;
  height: 100%;
  background: currentColor;
  opacity: .6;
  position: absolute;
  border-radius: 50%;
  animation: morph 1s linear infinite;
  box-shadow: 0 0 5px 1px currentColor;
  border: 9px solid;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="morph"]::after,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="morph"]::after {
  background: currentColor;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  height: 50%;
  border-radius: 50%;
  content: "";
  display: block;
}

/* target animation */
#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="target"],
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="target"]{
  height: 18px;
  width: 18px;
  box-shadow: 0 0 4px 2px currentColor;
  opacity: 1;
  animation: target 2s linear infinite;
  background: currentColor !important;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="target"]::before,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="target"]::before {
  content: "";
  display: block;
  position: absolute;
  top: 100%;
  left: 100%;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 10px 10px 0 0;
  border-color: currentColor transparent transparent transparent;
  opacity: .6;
  background: none;
  animation: none;
  border-radius: 0;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="target"]::after,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="target"]::after {
  content: "";
  display: block;
  position: absolute;
  bottom: 100%;
  right: 100%;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 0 10px 10px;
  border-color: transparent transparent currentColor transparent;
  opacity: .6;
  top: initial;
  left: initial;
  border-radius: initial;
  background: none;
}

 /* egg animations */
 #userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="egg"],
 #userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="egg"]{
  width: 18px;
  height: 18px;
  border-radius: 50%;
  position: relative;
  box-shadow: inset 0 0 6px 4px currentColor;
  animation: egg 600ms linear infinite;
  animation-direction: alternate;
  background: none !important;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="egg"]::before,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="egg"]::before {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  content: "";
  display: block;
  background: transparent;
  border: 1px solid currentColor;
  animation: none;
}

#userpilotContent[key=""]:not([version="0.1"]) .up-t-pluse[animation="egg"]::after,
#userpilotContent[key=""]:not([version="0.1"]) .userpilot-ripple[animation="egg"]::after {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  content: "";
  display: block;
  background: currentColor;
  opacity: .6;
}


@keyframes userpilotActive {
  0% {
    -webkit-transform: scale(.1);
    border-color: inherit;
    opacity: 1
  }

  30% {
    -webkit-transform: scale(1);
    border: 5px solid;
    border-color: inherit;
    opacity: 1
  }

  40% {
    -webkit-transform: scale(1.3);
    border: 0 solid;
    border-color: inherit
  }

  100% {
    border: 0 solid;
    border-color: inherit
  }
}

@-webkit-keyframes active {
  0% {
    -webkit-transform: scale(.1);
    border-color: inherit;
    opacity: 1
  }

  30% {
    -webkit-transform: scale(1);
    border: 5px solid;
    border-color: inherit;
    opacity: 1
  }

  40% {
    -webkit-transform: scale(1.3);
    border: 0 solid;
    border-color: inherit
  }

  100% {
    border: 0 solid;
    border-color: inherit
  }
}

@keyframes pulse-dot {
  0% {
    transform: scale(1, 1) translate(-50%, -50%);
  }

  30% {
    transform: scale(1.25, 1.25) translate(-40%, -40%);
  }

  100% {
    transform: scale(1, 1) translate(-50%, -50%);
  }
}

@keyframes pulse-ring {
  0% {
    transform: scale(1, 1);
    opacity: 0;
  }

  25% {
    opacity: .5;
  }

  100% {
    transform: scale(1.8, 1.8);
    opacity: 0;
  }
}

@keyframes morph {
  0% {
    transform: rotateZ(0);
    border-radius: 20%;
  }

  50% {
    transform: rotateZ(45deg);
    border-radius: 50%;
  }

  100% {
    transform: rotateZ(90deg);
    border-radius: 20%;
  }
}

@keyframes target {
  0% {
    transform: rotateZ(0) scale(0.6);
  }

  50% {
    transform: rotateZ(180deg) scale(1);
  }

  100% {
    transform: rotateZ(360deg) scale(0.6);
  }
}

@keyframes egg {
  from {
    box-shadow: inset 0 0 8px 3px currentColor;
  }

  to {
    box-shadow: inset 0 0 4px 1px currentColor;
  }
}</style><style nonce="undefined">
iframe#userpilotIframeContainer,
iframe#userpilotContentNativeIframe,
iframe#userpilot-nps,
iframe#userpilot-resource-centre-frame,
iframe#userpilot-checklist,
iframe#userpilotSurveys {
  max-height: none;
  max-width: none;
  min-height: 0px;
  min-width: 0px;
  filter: none;
  pointer-events: initial;
}

iframe#userpilotIframeContainer,
iframe#userpilotContentNativeIframe,
iframe#userpilot-resource-centre-frame,
iframe#userpilot-checklist,
iframe#userpilotSurveys {
  right: initial;
  left: initial;
}

iframe#userpilotIframeContainer,
iframe#userpilotContentNativeIframe,
iframe#userpilot-resource-centre-frame {
    display: initial;
}
</style></head>

  <body class="signed_in env_production notranslate" translate="no" data-theme-suffix="_alx">
      <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N4C8MF2"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->


      <input type="hidden" id="hbtn-slack-url" value="https://alx-students.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="" data-original-title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="" data-original-title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="" data-original-title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="" data-original-title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>
    

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Captain's Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain's Logs</div></a></li>


<hr class="visible-xs">

<li>

      <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>
</a>      </div>

  <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://intranet.alxswe.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBMVZmQnc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--9d22f07517e71e2136ed66f7b8389e27ea556cdd/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hKeVpYTnBlbVZmZEc5ZlptbDBXd2RwQWNocEFjZz0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--eb34eb1c984c21eb44bd7063b5c7194852f6e5a5/3FDD8E7E-31E2-437A-8A91-06DC98EE9865.jpeg')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>
    


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="" data-original-title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="" data-original-title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="" data-original-title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="" data-original-title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>
    

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Captain's Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain's Logs</div></a></li>


<hr class="visible-xs">

<li>

      <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>
</a>      </div>

  <div data-container="body" data-placement="right" data-toggle="tooltip" title="" data-original-title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://intranet.alxswe.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBMVZmQnc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--9d22f07517e71e2136ed66f7b8389e27ea556cdd/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hKeVpYTnBlbVZmZEc5ZlptbDBXd2RwQWNocEFjZz0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--eb34eb1c984c21eb44bd7063b5c7194852f6e5a5/3FDD8E7E-31E2-437A-8A91-06DC98EE9865.jpeg')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
        

        <div id="layout-bars">
          
          <div class="px-5 py-3" id="student-switch-curriculum">
  <div class="dropdown d-flex flex-column gap-1">
    <span class="fs-small text-muted">Curriculum</span>

    <div aria-haspopup="true" aria-expanded="false" class="align-items-center d-flex gap-3" data-toggle="dropdown" id="student-switch-curriculum-dropdown" role="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-600">
          SE Foundations
        </span>
        <span class="fs-small text-muted">
          Average: <span class="fw-500">128.04%</span>
        </span>
      </div>

      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-up  fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-down  fa-fw"></i>
        </span>
      </div>
    </div>

    <ul aria-labelledby="student-switch-curriculum-dropdown" class="dropdown-menu fs-5">
        <li>
          <a href="/curriculums/1/observe">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                  SE Foundations
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">128.04%</span>
                </span>
              </div>

                <span class="fw-600 text-info" style="margin-left: 42px">
                  <i aria-hidden="true" class="fa-solid fa-check "></i>
                </span>
            </div>
</a>        </li>
    </ul>
  </div>
</div>

          
          
          
        </div>

      <article class="">

        
  <div class="d-flex flex-wrap">

    <div class="flex-grow-1" id="curriculum_navigation_content">
      
<div class="project row">
  <div class="col-xs-12 col-lg-10 contains-images">

      <h1 class="gap">
    0x00. AirBnB clone - The console
    
  </h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:16,&quot;value&quot;:&quot;Group project&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:19,&quot;value&quot;:&quot;Python&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:27,&quot;value&quot;:&quot;OOP&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"><div class="align-items-center d-flex flex-wrap gap-3 my-2"><span class="label label-primary" style="font-size: 14px;">Group project</span><span class="label label-primary" style="font-size: 14px;">Python</span><span class="label label-primary" style="font-size: 14px;">OOP</span></div></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;weight&quot;:5,&quot;correction&quot;:{&quot;released&quot;:false,&quot;auto_correction_available_at&quot;:&quot;2024-05-18T12:00:00.000+03:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:true},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-05-13T06:00:00.000+03:00&quot;,&quot;ends_at&quot;:&quot;2024-05-20T06:00:00.000+03:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-05-22T06:00:00.000+03:00&quot;},&quot;team&quot;:{&quot;in_team_of&quot;:2,&quot;members&quot;:[&quot;Naoufel Boukarma&quot;,&quot;Ahmed Muawia&quot;]}}}" data-react-cache-id="projects/ProjectMetadata-0"><ul class="list-group metadata" id="project-metadata"><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-gear fa-fw"></i> Weight: 5</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-users fa-fw"></i> Project to be done in teams of 2 people (your team: Naoufel Boukarma, Ahmed Muawia)</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-calendar fa-fw"></i> Project will start <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-05-13 06:00 (GMT+03:00)"><span class="datetime">May 13, 2024 6:00 AM</span></span>, must end by <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-05-20 06:00 (GMT+03:00)"><span class="datetime">May 20, 2024 6:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-check fa-fw"></i> Checker will be released at <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-05-18 12:00 (GMT+03:00)"><span class="datetime">May 18, 2024 12:00 PM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-square-check fa-fw"></i> <strong>Manual QA review must be done</strong> (request it when you are done with the project)</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-square-check fa-fw"></i> An auto review will be launched at the deadline</li></ul></div>




    


    <div id="project_id" style="display: none" data-project-id="263"></div>



      

        <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Concepts</h3>
    </div>
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/66">Python packages</a>
          </li>
          <li>
            <a href="/concepts/74">AirBnB clone</a>
          </li>
      </ul>
    </div>
  </div>


      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=5389fbc6760a6b66d6e17c43869552d07cb637ec089d62a92ed3aa638d39a588" alt="" loading="lazy" style=""></p>

<h2>Background Context</h2>

<h3>Welcome to the AirBnB clone project!</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>…) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What’s a command interpreter?</h3>

<p>Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/8ecCwE6veBmm3Nppw4hz5A" title="cmd module" target="_blank">cmd module</a> </li>
<li><a href="/rltoken/uEy4RftSdKypoig9NFTvCg" title="cmd module in depth" target="_blank">cmd module in depth</a></li>
<li><strong>packages</strong> concept page</li>
<li><a href="/rltoken/KfL9TqwdI69W6ttG6gTPPQ" title="uuid module" target="_blank">uuid module</a> </li>
<li><a href="/rltoken/1d8I3jSKgnYAtA1IZfEDpA" title="datetime" target="_blank">datetime</a> </li>
<li><a href="/rltoken/IlFiMB8UmqBG2CxA0AD3jA" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/C_a0EKbtvKdMcwIAuSIZng" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/tgNVrKKzlWgS4dfl3mQklw" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
<li><a href="/rltoken/EvcaH9uTLlauxuw03WnkOQ" title="cmd module wiki page" target="_blank">cmd module wiki page</a></li>
<li><a href="/rltoken/begh14KQA-3ov29KvD_HvA" title="python unittest" target="_blank">python unittest</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/uV5eZkRZ_XEqYbgPd-0CWw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an <code>UUID</code></li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/op1-rQGlw0wwwqNBsn1yaw" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project</li>
<li>e.g., For <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>e.g., For <code>models/user.py</code>, unit tests must be in: <code>tests/test_models/test_user.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case</li>
</ul>

<h3>GitHub</h3>

<p><strong>There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.</strong></p>

<h2>More Info</h2>

<h3>Execution</h3>

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

<p>All tests should also pass in non-interactive mode: <code>$ echo "python3 -m unittest discover tests" | bash</code></p>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=576ede4c6880b3fb30d00758c37945988294cd2ed457c0924f0d9949968c7267" alt="" loading="lazy" style=""></p>

  </div>
</div>


        <div data-react-class="videos/PlayerLibrary" data-react-props="{&quot;canManageVideos&quot;:false,&quot;videos&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eHBNB project overview of each part\u003c/p\u003e\n&quot;,&quot;id&quot;:31,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=7173213042379d4b8720838a38296b04604a747f8d610ab2cff478eeb56b253c&quot;,&quot;shortDescription&quot;:&quot;HBNB project overview of each part&quot;,&quot;source&quot;:&quot;/video_releases/31.m3u8&quot;,&quot;title&quot;:&quot;HBNB project overview&quot;},{&quot;description&quot;:&quot;\u003cp\u003eThe console part of the AirBnB clone project\u003c/p\u003e\n&quot;,&quot;id&quot;:32,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=894f2f6c81bf54e5b43cdb1d0c3e22e03825c4a6e1694f291ddfce43928c3750&quot;,&quot;shortDescription&quot;:&quot;The console part of the AirBnB clone project&quot;,&quot;source&quot;:&quot;/video_releases/32.m3u8&quot;,&quot;title&quot;:&quot;HBNB - the console&quot;},{&quot;description&quot;:&quot;\u003cp\u003eUsage of UUID in Python\u003c/p\u003e\n&quot;,&quot;id&quot;:34,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=b70ee2e0afb3dd8abaf6c0a1639b5e8fdc1113351ba5b4901d90630ab4418052&quot;,&quot;shortDescription&quot;:&quot;Usage of UUID in Python&quot;,&quot;source&quot;:&quot;/video_releases/34.m3u8&quot;,&quot;title&quot;:&quot;Python: Unique Identifier&quot;},{&quot;description&quot;:&quot;\u003cp\u003eHow to create and design Python Unittests\u003c/p\u003e\n&quot;,&quot;id&quot;:35,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=8957f1a6ae35a846a96b3bbde12130d3bfe5b7bfa9b5b75055184aec89deafd8&quot;,&quot;shortDescription&quot;:&quot;How to create and design Python Unittests&quot;,&quot;source&quot;:&quot;/video_releases/35.m3u8&quot;,&quot;title&quot;:&quot;Python: Unittests&quot;},{&quot;description&quot;:&quot;\u003cp\u003ePython class, base model and inheritance in the AirBnB clone project\u003c/p\u003e\n&quot;,&quot;id&quot;:36,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=13f238044c7d3264c0ce78d2c38b6acfc4024115743ecfa9a461fc59d4ff871e&quot;,&quot;shortDescription&quot;:&quot;Python class, base model and inheritance in the AirBnB clone project&quot;,&quot;source&quot;:&quot;/video_releases/36.m3u8&quot;,&quot;title&quot;:&quot;Python: BaseModel and inheritance&quot;},{&quot;description&quot;:&quot;\u003cp\u003eGit usage and code consistency for better team work\u003c/p\u003e\n&quot;,&quot;id&quot;:37,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=2757067dcd3043c021fbf7f742d2698611da81a2eeea01c3cf1c4108d8f4824d&quot;,&quot;shortDescription&quot;:&quot;Git usage and code consistency for better team work&quot;,&quot;source&quot;:&quot;/video_releases/37.m3u8&quot;,&quot;title&quot;:&quot;Code consistency&quot;},{&quot;description&quot;:&quot;\u003cp\u003eCreation and usage of Python modules and packages\u003c/p\u003e\n&quot;,&quot;id&quot;:38,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=9b70da7373e693305bd1ba5179abc549e2e2d62ee90bcfdfe1ad8d7af3a5fbc0&quot;,&quot;shortDescription&quot;:&quot;Creation and usage of Python modules and packages&quot;,&quot;source&quot;:&quot;/video_releases/38.m3u8&quot;,&quot;title&quot;:&quot;Python: Modules and Packages&quot;},{&quot;description&quot;:&quot;\u003cp\u003eHow in the AirBnB clone project storage is managed: File and Database\u003c/p\u003e\n&quot;,&quot;id&quot;:40,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20240516T093822Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=a0a8db768b965b100c553561175238bc2de4698618abab381968f98bad70f181&quot;,&quot;shortDescription&quot;:&quot;How in the AirBnB clone project storage is managed&quot;,&quot;source&quot;:&quot;/video_releases/40.m3u8&quot;,&quot;title&quot;:&quot;HBNB - storage abstraction&quot;}]}" data-react-cache-id="videos/PlayerLibrary-0"><div><div class="panel panel-default sm-gap"><div class="panel-heading panel-heading-actions"><h3 class="panel-title">Video library<small style="margin-left: 8px;">(8 total)</small></h3></div><div class="list-group"><div class="list-group-item"><div class="align-items-center d-flex" style="position: relative; width: 100%;"><input class="form-control" placeholder="Search by title" type="search" value=""></div></div></div><div class="list-group"><div style="display: flex; flex-flow: wrap;"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="HBNB project overview of each part"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7173213042379d4b8720838a38296b04604a747f8d610ab2cff478eeb56b253c&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">HBNB project overview</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="The console part of the AirBnB clone project"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b/116354b1cc94450120edeb9156af51725f4e0b0d18c43030c626810f8ee3fb7b.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=894f2f6c81bf54e5b43cdb1d0c3e22e03825c4a6e1694f291ddfce43928c3750&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">HBNB - the console</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Usage of UUID in Python"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652/738d8f17874d91803de2e5c4f9ee5a20cb872390744505627d692bbb3945b652.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=b70ee2e0afb3dd8abaf6c0a1639b5e8fdc1113351ba5b4901d90630ab4418052&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">Python: Unique Identifier</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="How to create and design Python Unittests"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f/d9d017dfd1b9697b7f3d75af85aa7e2fec0397a04541a918fdc53f7a0513b21f.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8957f1a6ae35a846a96b3bbde12130d3bfe5b7bfa9b5b75055184aec89deafd8&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">Python: Unittests</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Python class, base model and inheritance in the AirBnB clone project"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b/4c8cf8b97eab59676c4330f8308a59b479978cbac4cb58928c8683129e62161b.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=13f238044c7d3264c0ce78d2c38b6acfc4024115743ecfa9a461fc59d4ff871e&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">Python: BaseModel and inheritance</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Git usage and code consistency for better team work"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a/a1621a12e252129ffa245698e37e5828b5a0118cc0a426db11fad50c74064e3a.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=2757067dcd3043c021fbf7f742d2698611da81a2eeea01c3cf1c4108d8f4824d&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">Code consistency</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Creation and usage of Python modules and packages"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c/da9dd761329eb52dbff900227e4d05041f0a62801110942e655fb7d7b3599a0c.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=9b70da7373e693305bd1ba5179abc549e2e2d62ee90bcfdfe1ad8d7af3a5fbc0&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">Python: Modules and Packages</div></div></span><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="How in the AirBnB clone project storage is managed"><div style="cursor: pointer; display: flex; flex-direction: column; margin: 10px;"><div style="position: relative;"><div style="background-color: rgb(0, 0, 0); background-image: url(&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd/b24d6365d9d5dcecfa1e2a854ccdb533d8e5ba4bb10db0bb6c192993f53b6cfd.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240516T093822Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a0a8db768b965b100c553561175238bc2de4698618abab381968f98bad70f181&quot;); background-position: center center; background-repeat: no-repeat; background-size: contain; border-radius: 3px; height: 126px; width: 224px;"></div></div><div style="-webkit-box-orient: vertical; -webkit-line-clamp: 2; display: -webkit-box; font-size: 1.4rem; font-weight: bold; line-height: 2rem; margin-top: 6px; max-height: 4rem; max-width: 192px; overflow: hidden; padding: 0px 4px; text-overflow: ellipsis; white-space: normal;">HBNB - storage abstraction</div></div></span></div></div></div></div></div>


      

        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1377" data-position="0" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1377">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. README, AUTHORS
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <ul>
<li>Write a <code>README.md</code>:

<ul>
<li>description of the project</li>
<li>description of the command interpreter:

<ul>
<li>how to start it</li>
<li>how to use it</li>
<li>examples</li>
</ul></li>
</ul></li>
<li>You should have an <code>AUTHORS</code> file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference <a href="/rltoken/_8n_z3pf5HWi1l7uv1E9iA" title="Docker's AUTHORS page" target="_blank">Docker’s AUTHORS page</a></li>
<li>You should use branches and pull requests on GitHub - it will help you as team to organize your work</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>README.md, AUTHORS</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1377">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1378" data-position="1" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1378">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Be pycodestyle compliant!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write beautiful code that passes the pycodestyle checks.</p>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1378">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1378}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1385" data-position="2" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1385">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Unittests
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>All your files, classes, functions must be tested with unit tests</p>

<pre><code>guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
</code></pre>

<p><em>Note that this is just an example, the number of tests you create can be different from the above example</em>.</p>

<p><strong>Warning:</strong></p>

<p>Unit tests must also pass in non-interactive mode:</p>

<pre><code>guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1385">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1385}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1379" data-position="3" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1379">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. BaseModel
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a class <code>BaseModel</code> that defines all common attributes/methods for other classes:</p>

<ul>
<li><code>models/base_model.py</code></li>
<li>Public instance attributes: 

<ul>
<li><code>id</code>: string - assign with an <code>uuid</code> when an instance is created:

<ul>
<li>you can use <code>uuid.uuid4()</code> to generate unique <code>id</code> but don’t forget to convert to a string</li>
<li>the goal is to have unique <code>id</code> for each <code>BaseModel</code></li>
</ul></li>
<li><code>created_at</code>: datetime - assign with the current datetime when an instance is created</li>
<li><code>updated_at</code>: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
</ul></li>
<li><code>__str__</code>: should print: <code>[&lt;class name&gt;] (&lt;self.id&gt;) &lt;self.__dict__&gt;</code></li>
<li>Public instance methods:

<ul>
<li><code>save(self)</code>: updates the public instance attribute <code>updated_at</code> with the current datetime</li>
<li><code>to_dict(self)</code>: returns a dictionary containing all keys/values of <code>__dict__</code> of the instance:

<ul>
<li>by using <code>self.__dict__</code>, only instance attributes set will be returned</li>
<li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
<li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:

<ul>
<li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: <code>2017-06-14T22:31:03.285259</code>) </li>
<li>you can use <code>isoformat()</code> of <code>datetime</code> object</li>
</ul></li>
<li>This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our <code>BaseModel</code></li>
</ul></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (&lt;class 'int'&gt;) - 89
    name: (&lt;class 'str'&gt;) - My First Model
    __class__: (&lt;class 'str'&gt;) - BaseModel
    updated_at: (&lt;class 'str'&gt;) - 2017-09-28T21:05:54.119572
    id: (&lt;class 'str'&gt;) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (&lt;class 'str'&gt;) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>models/base_model.py, models/__init__.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1379">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1379}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1984" data-position="4" id="task-num-4">
      <div class="panel panel-default task-card " id="task-1984">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Create BaseModel from dictionary
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Previously we created a method to generate a dictionary representation of an instance (method <code>to_dict()</code>).</p>

<p>Now it’s time to re-create an instance with this dictionary representation.</p>

<pre><code>&lt;class 'BaseModel'&gt; -&gt; to_dict() -&gt; &lt;class 'dict'&gt; -&gt; &lt;class 'BaseModel'&gt;
</code></pre>

<p>Update <code>models/base_model.py</code>:</p>

<ul>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>you will use <code>*args, **kwargs</code> arguments for the constructor of a <code>BaseModel</code>. (more information inside the <strong>AirBnB clone</strong> concept page)</li>
<li><code>*args</code> won’t be used</li>
<li>if <code>kwargs</code> is not empty:

<ul>
<li>each key of this dictionary is an attribute name (<strong>Note</strong> <code>__class__</code> from <code>kwargs</code> is the only one that should not be added as an attribute. See the example output, below)</li>
<li>each value of this dictionary is the value of this attribute name</li>
<li><strong>Warning</strong>: <code>created_at</code> and <code>updated_at</code> are strings in this dictionary, but inside your <code>BaseModel</code> instance is working with <code>datetime</code> object. You have to convert these strings into <code>datetime</code> object. Tip: you know the string format of these datetime</li>
</ul></li>
<li>otherwise:

<ul>
<li>create <code>id</code> and <code>created_at</code> as you did previously (new instance)</li>
</ul></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
&lt;class 'datetime.datetime'&gt;
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (&lt;class 'str'&gt;) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (&lt;class 'str'&gt;) - 2017-09-28T21:03:54.052298
    __class__: (&lt;class 'str'&gt;) - BaseModel
    my_number: (&lt;class 'int'&gt;) - 89
    updated_at: (&lt;class 'str'&gt;) - 2017-09-28T21:03:54.052302
    name: (&lt;class 'str'&gt;) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
&lt;class 'datetime.datetime'&gt;
--
False
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>models/base_model.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1984">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1984}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1380" data-position="5" id="task-num-5">
      <div class="panel panel-default task-card " id="task-1380">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Store first object
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Now we can recreate a <code>BaseModel</code> from another one by using a dictionary representation:</p>

<pre><code>&lt;class 'BaseModel'&gt; -&gt; to_dict() -&gt; &lt;class 'dict'&gt; -&gt; &lt;class 'BaseModel'&gt;
</code></pre>

<p>It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.</p>

<p>Writing the dictionary representation to a file won’t be relevant:</p>

<ul>
<li>Python doesn’t know how to convert a string to a dictionary (easily)</li>
<li>It’s not human readable</li>
<li>Using this file with another program in Python or other language will be hard.</li>
</ul>

<p>So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.</p>

<p>Now the flow of serialization-deserialization will be:</p>

<pre><code>&lt;class 'BaseModel'&gt; -&gt; to_dict() -&gt; &lt;class 'dict'&gt; -&gt; JSON dump -&gt; &lt;class 'str'&gt; -&gt; FILE -&gt; &lt;class 'str'&gt; -&gt; JSON load -&gt; &lt;class 'dict'&gt; -&gt; &lt;class 'BaseModel'&gt;
</code></pre>

<p>Magic right?</p>

<p>Terms:</p>

<ul>
<li><strong>simple Python data structure</strong>: Dictionaries, arrays, number and string. ex: <code>{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }</code></li>
<li><strong>JSON string representation</strong>: String representing a simple data structure in JSON format. ex: <code>'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'</code></li>
</ul>

<p>Write a class <code>FileStorage</code> that serializes instances to a JSON file and deserializes JSON file to instances:</p>

<ul>
<li><code>models/engine/file_storage.py</code></li>
<li>Private class attributes:

<ul>
<li><code>__file_path</code>: string - path to the JSON file (ex: <code>file.json</code>)</li>
<li><code>__objects</code>: dictionary - empty but will store all objects by <code>&lt;class name&gt;.id</code> (ex: to store a <code>BaseModel</code> object with <code>id=12121212</code>, the key will be <code>BaseModel.12121212</code>)</li>
</ul></li>
<li>Public instance methods:

<ul>
<li><code>all(self)</code>: returns the dictionary <code>__objects</code></li>
<li><code>new(self, obj)</code>: sets in <code>__objects</code> the <code>obj</code> with key <code>&lt;obj class name&gt;.id</code></li>
<li><code>save(self)</code>: serializes <code>__objects</code> to the JSON file (path: <code>__file_path</code>)</li>
<li><code>reload(self)</code>: deserializes the JSON file to <code>__objects</code> (only if the JSON file (<code>__file_path</code>) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)</li>
</ul></li>
</ul>

<p>Update <code>models/__init__.py</code>: to create a unique <code>FileStorage</code> instance for your application</p>

<ul>
<li>import <code>file_storage.py</code></li>
<li>create the variable <code>storage</code>, an instance of <code>FileStorage</code></li>
<li>call <code>reload()</code> method on this variable</li>
</ul>

<p>Update <code>models/base_model.py</code>: to link your <code>BaseModel</code> to <code>FileStorage</code> by using the variable <code>storage</code></p>

<ul>
<li>import the variable <code>storage</code></li>
<li>in the method <code>save(self)</code>:

<ul>
<li>call <code>save(self)</code> method of <code>storage</code></li>
</ul></li>
<li><code>__init__(self, *args, **kwargs)</code>: 

<ul>
<li>if it’s a new instance (not from a dictionary representation), add a call to the method <code>new(self)</code> on <code>storage</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1380">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1380}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1376" data-position="6" id="task-num-6">
      <div class="panel panel-default task-card " id="task-1376">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Console 0.0.1
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a program called <code>console.py</code> that contains the entry point of the command interpreter:</p>

<ul>
<li>You must use the module <code>cmd</code></li>
<li>Your class definition must be: <code>class HBNBCommand(cmd.Cmd):</code></li>
<li>Your command interpreter should implement:

<ul>
<li><code>quit</code> and <code>EOF</code> to exit the program</li>
<li><code>help</code> (this action is provided by default by <code>cmd</code> but you should keep it updated and documented as you work through tasks)</li>
<li>a custom prompt: <code>(hbnb)</code></li>
<li>an empty line + <code>ENTER</code> shouldn’t execute anything</li>
</ul></li>
<li>Your code should not be executed when imported</li>
</ul>

<p><strong>Warning:</strong></p>

<p>You should end your file with:</p>

<pre><code>if __name__ == '__main__':
    HBNBCommand().cmdloop()
</code></pre>

<p>to make your program executable except when imported.
Please don’t add anything around - the Checker won’t like it otherwise</p>

<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

<p><strong>No unittests needed</strong></p>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>console.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1376">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1376}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1381" data-position="7" id="task-num-7">
      <div class="panel panel-default task-card " id="task-1381">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Console 0.1
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Update your command interpreter (<code>console.py</code>) to have these commands:</p>

<ul>
<li><code>create</code>: Creates a new instance of <code>BaseModel</code>, saves it (to the JSON file) and prints the <code>id</code>. Ex: <code>$ create BaseModel</code> 

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ create</code>)</li>
<li>If the class name doesn’t exist, print <code>** class doesn't exist **</code> (ex: <code>$ create MyModel</code>)</li>
</ul></li>
<li><code>show</code>: Prints the string representation of an instance based on the class name and <code>id</code>. Ex: <code>$ show BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ show</code>)</li>
<li>If the class name doesn’t exist, print <code>** class doesn't exist **</code> (ex: <code>$ show MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ show BaseModel</code>)</li>
<li>If the instance of the class name doesn’t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ show BaseModel 121212</code>)</li>
</ul></li>
<li><code>destroy</code>: Deletes an instance based on the class name and <code>id</code> (save the change into the JSON file). Ex: <code>$ destroy BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ destroy</code>)</li>
<li>If the class name doesn’t exist, print <code>** class doesn't exist ** (ex:</code>$ destroy MyModel<code>)</code></li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ destroy BaseModel</code>)</li>
<li>If the instance of the class name doesn’t exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ destroy BaseModel 121212</code>)</li>
</ul></li>
<li><code>all</code>: Prints all string representation of all instances based or not on the class name. Ex: <code>$ all BaseModel</code> or <code>$ all</code>.

<ul>
<li>The printed result must be a list of strings (like the example below)</li>
<li>If the class name doesn’t exist, print <code>** class doesn't exist **</code> (ex: <code>$ all MyModel</code>)</li>
</ul></li>
<li><code>update</code>: Updates an instance based on the class name and <code>id</code> by adding or updating attribute (save the change into the JSON file). Ex: <code>$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"</code>.

<ul>
<li>Usage: <code>update &lt;class name&gt; &lt;id&gt; &lt;attribute name&gt; "&lt;attribute value&gt;"</code></li>
<li>Only one attribute can be updated at the time</li>
<li>You can assume the attribute name is valid (exists for this model)</li>
<li>The attribute value must be casted to the attribute type </li>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ update</code>)</li>
<li>If the class name doesn’t exist, print <code>** class doesn't exist **</code> (ex: <code>$ update MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ update BaseModel</code>)</li>
<li>If the instance of the class name doesn’t exist for the <code>id</code>, print <code>** no instance found **</code>  (ex: <code>$ update BaseModel 121212</code>)</li>
<li>If the attribute name is missing, print <code>** attribute name missing **</code> (ex: <code>$ update BaseModel existing-id</code>)</li>
<li>If the value for the attribute name doesn’t exist, print <code>** value missing **</code> (ex: <code>$ update BaseModel existing-id first_name</code>)</li>
<li>All other arguments should not be used (Ex: <code>$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"</code> = <code>$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"</code>)</li>
<li><code>id</code>, <code>created_at</code> and <code>updated_at</code> cant’ be updated. You can assume they won’t be passed in the <code>update</code> command</li>
<li>Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime</li>
</ul></li>
</ul>

<p>Let’s add some rules:</p>

<ul>
<li>You can assume arguments are always in the right order</li>
<li>Each arguments are separated by a space</li>
<li>A string argument with a space must be between double quote</li>
<li>The error management starts from the first argument to the last one<br></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
</code></pre>

<p><strong>No unittests needed</strong></p>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>console.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1381">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1381}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1382" data-position="8" id="task-num-8">
      <div class="panel panel-default task-card " id="task-1382">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. First User
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a class <code>User</code> that inherits from <code>BaseModel</code>:</p>

<ul>
<li><code>models/user.py</code></li>
<li>Public class attributes:

<ul>
<li><code>email</code>: string - empty string</li>
<li><code>password</code>: string - empty string</li>
<li><code>first_name</code>: string - empty string</li>
<li><code>last_name</code>: string - empty string</li>
</ul></li>
</ul>

<p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of <code>User</code>.</p>

<p>Update your command interpreter (<code>console.py</code>) to allow <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> used with <code>User</code>.</p>

<pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>

<p><strong>No unittests needed for the console</strong></p>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>models/user.py, models/engine/file_storage.py, console.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1382">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1382}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1383" data-position="9" id="task-num-9">
      <div class="panel panel-default task-card " id="task-1383">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. More classes!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write all those classes that inherit from <code>BaseModel</code>:</p>

<ul>
<li><code>State</code> (<code>models/state.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>City</code> (<code>models/city.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>state_id</code>: string - empty string: it will be the <code>State.id</code></li>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Amenity</code> (<code>models/amenity.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Place</code> (<code>models/place.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>city_id</code>: string - empty string: it will be the <code>City.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>name</code>: string - empty string</li>
<li><code>description</code>: string - empty string</li>
<li><code>number_rooms</code>: integer - 0</li>
<li><code>number_bathrooms</code>: integer - 0</li>
<li><code>max_guest</code>: integer - 0</li>
<li><code>price_by_night</code>: integer - 0</li>
<li><code>latitude</code>: float - 0.0</li>
<li><code>longitude</code>: float - 0.0</li>
<li><code>amenity_ids</code>: list of string - empty list: it will be the list of <code>Amenity.id</code> later</li>
</ul></li>
</ul></li>
<li><code>Review</code> (<code>models/review.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>place_id</code>: string - empty string: it will be the <code>Place.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>text</code>: string - empty string</li>
</ul></li>
</ul></li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1383">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1383}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1384" data-position="10" id="task-num-10">
      <div class="panel panel-default task-card " id="task-1384">
  <span id="user_id" data-id="508788"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Console 1.0
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="508788"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code></p>

<p>Update your command interpreter (<code>console.py</code>) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.</p>

<p>Enjoy your first console!</p>

<p><strong>No unittests needed for the console</strong></p>

  </div>

  <div class="list-group">
    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>AirBnB_clone</code></li>
            <li>File: <code>console.py, models/engine/file_storage.py, tests/</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1384">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1384}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>

    <p class="lg-gap">
      </p><form class="button_to" method="post" action="/projects/263/unlock_optionals"><input id="unlock_optional_btn" class="btn btn-primary btn-block" data-confirm="Are you sure? Make sure you focused on the mandatory tasks first" data-disable-with="Unlocking 7 advanced tasks..." data-gtm-custom-event-name="project_unlock_advanced_tasks" type="submit" value="Done with the mandatory tasks? Unlock 7 advanced tasks now!"><input type="hidden" name="authenticity_token" value="LsAw9q1pLLXPeapmG3br2B1enzLsdIqtG5DMWYbRboitYEiXD-nv4_WHtzrWL0mdYUh43aex-_a6839D7pMNvg" autocomplete="off"></form>
    <p></p>


            <div data-react-class="projects/ProjectReadyForReview" data-react-props="{&quot;csrfToken&quot;:&quot;GlPQyhXWVde16GO9L7J1CtWd__dXP9LfwENhnFawW5qZ86irt1aWgY8WfuHi69dPqYsYGBz6o4RhINKGPvI4rA&quot;,&quot;firstReview&quot;:true,&quot;peerReview&quot;:{&quot;availableReviewersURI&quot;:&quot;/corrections/32378821/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:false,&quot;cancelReadyForReviewURI&quot;:&quot;/corrections/32378821/cancel_ready_for_review.json&quot;,&quot;closeAt&quot;:&quot;2024-05-22T06:00:00.000+03:00&quot;,&quot;correctCorrectionURI&quot;:&quot;https://intranet.alxswe.com/corrections/32378821/correct&quot;,&quot;disabled&quot;:false,&quot;manualReviewBehavior&quot;:&quot;reviewed_students&quot;,&quot;openAt&quot;:&quot;2024-05-13T06:00:00.000+03:00&quot;,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/32378821/toggle_ready_for_review.json&quot;,&quot;synchronousManualReview&quot;:false},&quot;toggled&quot;:false}" data-react-cache-id="projects/ProjectReadyForReview-0"><div class="row gap"><div class="col-md-12"><div class="text-center"><button class="btn btn-lg btn-primary">Ready for a  review</button></div></div></div></div>

          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;available&quot;:true,&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true,&quot;container&quot;:{&quot;container_id&quot;:&quot;57430a8955f3c9c9d89e3f3172ec29445abd401791cf0f675e2404cf7099a4fb&quot;,&quot;id&quot;:611012,&quot;restart_uri&quot;:&quot;/user_containers/611012/restart.json&quot;,&quot;status&quot;:&quot;running&quot;,&quot;uri&quot;:&quot;/user_containers/611012.json&quot;,&quot;wake_uri&quot;:&quot;/user_containers/611012/wake.json&quot;,&quot;webterm_uri&quot;:&quot;/user_containers/611012/webterm&quot;,&quot;host&quot;:&quot;57430a8955f3.8fd67979.alx-cod.online&quot;,&quot;password&quot;:&quot;13a902312f543a0adba9&quot;,&quot;ports&quot;:{&quot;4000&quot;:59413,&quot;5000&quot;:59412,&quot;5001&quot;:59411,&quot;8080&quot;:59409,&quot;22&quot;:59418,&quot;3306&quot;:59414,&quot;443&quot;:59416,&quot;80&quot;:59417,&quot;8000&quot;:59410,&quot;3000&quot;:59415}}}],&quot;containersLimit&quot;:2,&quot;csrfToken&quot;:&quot;k25Ng1joLHE76LyeFLT_Um0JKrqL1JTdb7g5_VHohA8QzjXi-mjvJwEWocLZ7V0XER_NVcAR5YbO24rnOarnOQ&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"><div><div class="d-flex gap-4 sandboxes-filters"><a class="btn btn-outline-primary"><i aria-hidden="true" class="fa-solid fa-filter"></i><span class="ml-2">Running only</span></a><div class="align-items-center d-flex" style="position: relative; width: 100%;"><input class="form-control" placeholder="Search for an image ..." type="search" value=""></div></div><div class="mt-3"><h3>1 image<small class="ml-2">(1/2 Sandboxes spawned)</small></h3></div><div class="mt-3"><div class="panel panel-default"><div class="panel-body border-left-success" style="border-left: 6px solid;"><div class="align-items-center d-flex flex-wrap justify-content-between"><div><h3 class="mt-0"><i aria-hidden="true" class="fa-solid fa-terminal text-success"></i><span class="ml-2">Ubuntu 20.04</span></h3><div class="mt-2 text-muted"><p>Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations</p>
</div></div><div class="d-flex flex-wrap gap-5"><div class="align-items-center d-flex gap-3"><div><span data-container="body" data-html="false" data-placement="top" data-toggle="tooltip" title="" data-original-title="Copy SSH command"><span role="button"><button class="btn btn-default">SSH</button></span></span></div><div><span data-container="body" data-html="false" data-placement="top" data-toggle="tooltip" title="" data-original-title="Copy SFTP command"><span role="button"><button class="btn btn-default">SFTP</button></span></span></div><a class="btn btn-webterm" href="/user_containers/611012/webterm" rel="noreferrer" target="_blank"><i aria-hidden="true" class="fa-solid fa-terminal"></i><span class="ml-2">Webterm</span></a></div><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Restart your Sandbox"><a class="btn btn-warning "><i aria-hidden="true" class="fa-solid fa-power-off"></i><span class="ml-2">Restart</span></a></span><a class="btn btn-danger"><i aria-hidden="true" class="fa-solid fa-trash"></i><span class="ml-2">Destroy</span></a></div></div><div class="d-flex flex-wrap gap-5 mt-3"><div class="p-4" style="flex-shrink: 0;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-user text-info"></i><span class="ml-2">Credentials</span></h4><div class="d-flex gap-2"><strong>Host</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>57430a8955f3.8fd67979.alx-cod.online</small></span></span></div><div class="d-flex gap-2"><strong>Username</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>57430a8955f3</small></span></span></div><div class="d-flex gap-2"><strong>Password</strong><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><small>13a902312f543a0adba9</small></span></span></div></div></div><div class="p-4" style="flex: 1 1 40%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-globe text-info"></i><span class="ml-2">Web access</span></h4><div class="align-items-center d-flex flex-wrap gap-2"><a class="btn btn-outline-primary" href="https://57430a8955f3.8fd67979.alx-cod.online" rel="noreferrer" target="_blank">HTTPS</a><a class="btn btn-outline-primary" href="http://57430a8955f3.8fd67979.alx-cod.online" rel="noreferrer" target="_blank">HTTP</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:3000" rel="noreferrer" target="_blank">3000</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:4000" rel="noreferrer" target="_blank">4000</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:5000" rel="noreferrer" target="_blank">5000</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:5001" rel="noreferrer" target="_blank">5001</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:8000" rel="noreferrer" target="_blank">8000</a><a class="btn btn-default" href="http://57430a8955f3.8fd67979.alx-cod.online:8080" rel="noreferrer" target="_blank">8080</a></div></div></div><div class="p-4" style="flex: 1 1 35%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-signs-post text-info"></i><span class="ml-2">Port mapping</span></h4><div class="align-items-center d-flex flex-wrap"><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>SSH</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59418</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTP</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59417</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTPS</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59416</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>3000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59415</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>MySQL</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59414</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>4000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59413</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59412</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5001</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59411</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59410</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8080</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>59409</span></div></div></div></div></div></div></div></div></div></div></div></div></div></div>

  </div>
</div>


      
    </div>
  </div>


      </article>

      <div class="copyright">Copyright © 2024 ALX, All rights reserved.</div>

    </main><script type="text/javascript" id="">window.userpilotSettings={token:"NX-b636a33d"};</script>
<script type="text/javascript" id="" src="https://js.userpilot.io/sdk/latest.js"></script><link rel="stylesheet" href="https://alx-tools.github.io/savanna-content-styles/assets/css/styles.css">

        <button class="btn btn-primary atop-help" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
  <i aria-hidden="true" class="fa-solid fa-magnifying-glass "></i>
  <i aria-hidden="true" class="fa-solid fa-window-minimize "></i>
</button>

        <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar" autocomplete="off" type="text" name="hbtn-search-bar" placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>



        <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>&gt; This is a quote.
&gt; It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


        <script id="cody-snippet">
          window.codySettings = { widget_id: "9993bc72-2258-452b-a4bf-b2fe1ad5e0d7" };
          !function(){var t=window,e=document,a=function(){var t=e.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://trinketsofcody.com/cody-widget.js";var a=e.getElementsByTagName("script")[0];a.parentNode.insertBefore(t,a)};"complete"===document.readyState?a():t.attachEvent?t.attachEvent("onload",a):t.addEventListener("load",a,!1)}();
        </script>
  

<iframe id="_hjSafeContext_66150175" title="_hjSafeContext" tabindex="-1" aria-hidden="true" src="about:blank" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe>
<script type="text/javascript" id="">for(var dl=window.dataLayer||[],user=void 0,i=0;i<dl.length;i++)if(dl[i].userId){user=dl[i];break}user&&user.batch&&user.curriculum&&(userpilot.identify("savanna-"+user.userId.toString(),{cohortId:user.batch.id,cohortName:user.batch.fullNameWithC,locationId:user.batch.schoolLocation.id,locationName:user.batch.schoolLocation.name,curriculumId:user.curriculum.id,curriculumName:user.curriculum.name}),userpilot.reload());</script>
<div id="userpilotContent" key="" theme_id="0"></div><div id="cody-wrapper"><style>
  #cody-wrapper .cody-launcher {
    position: var(--position) !important;
    left: var(--left) !important;
    right: var(--right) !important;
    bottom: var(--launcher-bottom) !important;
    border-radius: 9999px !important;
    border: 0 !important;
    padding: 0 !important;
    box-sizing: border-box !important;
    z-index: 999999 !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: box-shadow, scale 300ms linear !important;
    animation: cody-launcher-pulse 4s infinite !important;
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
    cursor: pointer !important;
    --icon-margin: 12px;
    --close-icon-margin: 16px;
  }

    #cody-wrapper {
    --position: fixed;
    --left: unset;
    --right: 20px;
    --launcher-bottom: 20px;
    --frame-bottom: 90px;
    --background-color: #FBD647;
    --text-color: #020617;
    --shadow-color: 251, 214, 71;
  }

  @media screen and (max-width: 512px) {
    #cody-wrapper {
      --left: unset;
      --right: 10px;
    }
  }

  
  #cody-wrapper .cody-launcher:hover {
    scale: 1.1 !important;
  }

  #cody-wrapper .cody-launcher .cody-close-icon {
    display: none !important;
  }

  #cody-wrapper[data-launcher-open] .cody-launcher .cody-icon {
    display: none !important;;
  }

  #cody-wrapper[data-launcher-open] .cody-launcher .cody-close-icon {
    display: block !important;;
  }

  #cody-wrapper .cody-iframe {
    z-index: 99999 !important;
    transition: visibility .5s, opacity .5s linear !important;
    background-color: #fff !important;
    position: fixed !important;
    left: var(--left) !important;
    right: var(--right) !important;
    bottom: var(--frame-bottom) !important;
    height: 75vh !important;
    width: 448px !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 2px 4px rgba(0, 18, 26, .08), 0 3px 12px rgba(0, 18, 26, .16), 0 2px 14px 0 rgba(0, 18, 26, .2) !important;
    border: 0 !important;
    display: none !important;
  }

  @media screen and (max-height: 667px) {
    #cody-wrapper .cody-iframe {
      height: calc(100vh - 110px) !important;
    }
  }

  @media screen and (max-width: 448px) {
    #cody-wrapper .cody-iframe {
      width: calc(100vw - 20px) !important;
    }
  }

  #cody-wrapper[data-launcher-open] .cody-iframe {
    display: block !important;
  }

  @keyframes cody-launcher-pulse {
    0%, 100% {
      box-shadow: 0 0 18px 4px rgba(var(--shadow-color), 0.8);
    }
    50% {
      box-shadow: 0 0 12px 3px rgba(var(--shadow-color), 0.4);
    }
  }
</style>

<button class="cody-launcher" style="width: 56px; height: 56px; font-size: 16px;">
    <svg class="cody-icon" style="aspect-ratio: 1 / 1; width: 100%; height: 100%; margin: var(--icon-margin)" aria-hidden="true" viewBox="5 7 45 45" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <path d="M41.18 17.86a52.75 52.75 0 0 0-19 0c-.54.1-7.9 2.7-7.9 2.7h.01c-2.9 1.01-4.91 3.75-4.91 6.9v4.85c0 2.96 1.78 5.56 4.4 6.7l17.91 8.93v-6.67c3.18 0 6.36-.29 9.5-.86 4.13-.76 7.13-4.36 7.13-8.56v-5.44c-.01-4.19-3.01-7.79-7.14-8.55zm3.47 14c0 2.43-1.74 4.52-4.13 4.95-2.91.53-5.88.8-8.84.8s-5.93-.27-8.84-.8c-2.39-.44-4.13-2.52-4.13-4.95v-5.44c0-2.43 1.74-4.52 4.13-4.95 2.91-.53 5.88-.8 8.84-.8s5.93.27 8.84.8c2.39.44 4.13 2.52 4.13 4.95v5.44z" fill="currentColor"></path>
    <path d="M26.17 32.79c-.84 0-1.53-.68-1.53-1.53v-4.24c0-.84.68-1.53 1.53-1.53s1.53.68 1.53 1.53v4.24c-.01.85-.69 1.53-1.53 1.53zM37.17 32.79c-.84 0-1.53-.68-1.53-1.53v-4.24c0-.84.68-1.53 1.53-1.53s1.53.68 1.53 1.53v4.24c0 .85-.68 1.53-1.53 1.53z" fill="currentColor"></path>
</svg>    <svg style="aspect-ratio: 1/1; width: 100%; height: 100%; margin: var(--close-icon-margin);" class="cody-close-icon" launchercloseicon="chevron-down" aria-hidden="true" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
    <path d="M239 401c9.4 9.4 24.6 9.4 33.9 0L465 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-175 175L81 175c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9L239 401z" fill="currentColor"></path>
</svg></button></div></body></html>
