



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>matplotlib_pydata2013/simple_cube.py at master · jakevdp/matplotlib_pydata2013 · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="jakevdp/matplotlib_pydata2013" name="twitter:title" /><meta content="matplotlib_pydata2013 - PyData SV 2013 Tutorial on Hard code Matplotlib" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/781659?v=3&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/781659?v=3&amp;s=400" property="og:image" /><meta content="jakevdp/matplotlib_pydata2013" property="og:title" /><meta content="https://github.com/jakevdp/matplotlib_pydata2013" property="og:url" /><meta content="matplotlib_pydata2013 - PyData SV 2013 Tutorial on Hard code Matplotlib" property="og:description" />

      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="C29C2C07:1593:15C983B:54901CA7" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="KpXOqW6DWHqSv9lsyrg1z6mLb8iB4i0FFpONRJApKHGpV+Rwo3QOP3eWozRNAgGT93W6Emr8desj4rWTg9YQ4g==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-c7f434a471766a748d862b4cb294526acd6901321d901cc64028f53af8490603.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-761398b51b4a87682bde8f8b3479da06f8bde788a3fae6fb10b018a384748cf0.css" media="all" rel="stylesheet" type="text/css" />
    
    


    <meta http-equiv="x-pjax-version" content="52744ce9703c979de4f8f2f444b85ff4">

      
  <meta name="description" content="matplotlib_pydata2013 - PyData SV 2013 Tutorial on Hard code Matplotlib">
  <meta name="go-import" content="github.com/jakevdp/matplotlib_pydata2013 git https://github.com/jakevdp/matplotlib_pydata2013.git">

  <meta content="781659" name="octolytics-dimension-user_id" /><meta content="jakevdp" name="octolytics-dimension-user_login" /><meta content="8787602" name="octolytics-dimension-repository_id" /><meta content="jakevdp/matplotlib_pydata2013" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="8787602" name="octolytics-dimension-repository_network_root_id" /><meta content="jakevdp/matplotlib_pydata2013" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/jakevdp/matplotlib_pydata2013/commits/master.atom" rel="alternate" title="Recent Commits to matplotlib_pydata2013:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" ga-data-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="button primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="button" href="/login?return_to=%2Fjakevdp%2Fmatplotlib_pydata2013%2Fblob%2Fmaster%2Fnotebooks%2Ftutorial_lib%2Fsimple_cube.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <form accept-charset="UTF-8" action="/jakevdp/matplotlib_pydata2013/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/jakevdp/matplotlib_pydata2013/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="(Logged out) Header, go to blog, text:blog">Blog</a>
          </li>
      </ul>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">


  <li>
      <a href="/login?return_to=%2Fjakevdp%2Fmatplotlib_pydata2013"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/jakevdp/matplotlib_pydata2013/stargazers">
      39
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fjakevdp%2Fmatplotlib_pydata2013"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/jakevdp/matplotlib_pydata2013/network" class="social-count">
        16
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/jakevdp" class="url fn" itemprop="url" rel="author"><span itemprop="title">jakevdp</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/jakevdp/matplotlib_pydata2013" class="js-current-repository" data-pjax="#js-repo-pjax-container">matplotlib_pydata2013</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/jakevdp/matplotlib_pydata2013/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/jakevdp/matplotlib_pydata2013" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /jakevdp/matplotlib_pydata2013">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/jakevdp/matplotlib_pydata2013/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /jakevdp/matplotlib_pydata2013/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/jakevdp/matplotlib_pydata2013/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /jakevdp/matplotlib_pydata2013/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>


  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/jakevdp/matplotlib_pydata2013/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /jakevdp/matplotlib_pydata2013/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/jakevdp/matplotlib_pydata2013/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /jakevdp/matplotlib_pydata2013/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/jakevdp/matplotlib_pydata2013.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/jakevdp/matplotlib_pydata2013" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a> or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button" title="Save jakevdp/matplotlib_pydata2013 to your computer and use it in GitHub Desktop." aria-label="Save jakevdp/matplotlib_pydata2013 to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/jakevdp/matplotlib_pydata2013/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of jakevdp/matplotlib_pydata2013 as a zip file"
                   title="Download the contents of jakevdp/matplotlib_pydata2013 as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/jakevdp/matplotlib_pydata2013/blob/ed4e30ad9b461e5196dfc27d6488613ebc17c87a/notebooks/tutorial_lib/simple_cube.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:98a0c2e3e50c67ce4450d6c624046939 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/jakevdp/matplotlib_pydata2013/blob/master/notebooks/tutorial_lib/simple_cube.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/jakevdp/matplotlib_pydata2013/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/jakevdp/matplotlib_pydata2013" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">matplotlib_pydata2013</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/jakevdp/matplotlib_pydata2013/tree/master/notebooks" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">notebooks</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/jakevdp/matplotlib_pydata2013/tree/master/notebooks/tutorial_lib" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">tutorial_lib</span></a></span><span class="separator">/</span><strong class="final-path">simple_cube.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/jakevdp/matplotlib_pydata2013/contributors/master/notebooks/tutorial_lib/simple_cube.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>70 lines (55 sloc)</span>
          <span class="meta-divider"></span>
        <span>2.314 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/jakevdp/matplotlib_pydata2013/raw/master/notebooks/tutorial_lib/simple_cube.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/jakevdp/matplotlib_pydata2013/blame/master/notebooks/tutorial_lib/simple_cube.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/jakevdp/matplotlib_pydata2013/commits/master/notebooks/tutorial_lib/simple_cube.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="http://windows.github.com" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

            <a class="octicon-button disabled tooltipped tooltipped-w" href="#"
               aria-label="You must be signed in to make or propose changes"><span class="octicon octicon-pencil"></span></a>

          <a class="octicon-button danger disabled tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> plt</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-k">from</span> projection <span class="pl-k">import</span> Quaternion, project_points</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">Cube</span>(<span class="pl-e"><span class="pl-s3">object</span></span>):</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">    <span class="pl-s1"><span class="pl-pds">&quot;&quot;&quot;</span>An Axes for displaying a 3D cube<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">    <span class="pl-c"># fiducial face is perpendicular to z at z=+1</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line">    one_face <span class="pl-k">=</span> np.array([[<span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>], [<span class="pl-c1">1</span>, <span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">1</span>], [<span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">1</span>],</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">                         [<span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>], [<span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>]])</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">    <span class="pl-c"># Construct six rotators for the cube faces. These will take a single</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">    <span class="pl-c"># fiducial face, and rotate it to the appropriate 3D location.</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">    x, y, z <span class="pl-k">=</span> np.eye(<span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">    _rots <span class="pl-k">=</span> [Quaternion.from_v_theta(x, theta)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">             <span class="pl-k">for</span> theta <span class="pl-k">in</span> (np.pi <span class="pl-k">/</span> <span class="pl-c1">2</span>, <span class="pl-k">-</span>np.pi <span class="pl-k">/</span> <span class="pl-c1">2</span>)]</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">    _rots <span class="pl-k">+=</span> [Quaternion.from_v_theta(y, theta)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">              <span class="pl-k">for</span> theta <span class="pl-k">in</span> (np.pi <span class="pl-k">/</span> <span class="pl-c1">2</span>, <span class="pl-k">-</span>np.pi <span class="pl-k">/</span> <span class="pl-c1">2</span>, np.pi, <span class="pl-c1">2</span> <span class="pl-k">*</span> np.pi)]</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">    _faces <span class="pl-k">=</span> np.array([np.dot(one_face, rot.as_rotation_matrix().T)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">                       <span class="pl-k">for</span> rot <span class="pl-k">in</span> _rots])</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__init__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">view</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">10</span>), <span class="pl-vpf">colors</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-vpf">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.8</span>):</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">        <span class="pl-v">self</span>.view <span class="pl-k">=</span> view</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line">        <span class="pl-v">self</span>.current_rotation <span class="pl-k">=</span> Quaternion.from_v_theta((<span class="pl-c1">0</span>, <span class="pl-c1">0</span>, <span class="pl-c1">1</span>), <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line">        <span class="pl-k">if</span> colors <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">            colors <span class="pl-k">=</span> [<span class="pl-s1"><span class="pl-pds">&#39;</span>blue<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>green<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>white<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>yellow<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>orange<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>red<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">            <span class="pl-k">assert</span> <span class="pl-s3">len</span>(colors) <span class="pl-k">==</span> <span class="pl-c1">6</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">        <span class="pl-v">self</span>.polys <span class="pl-k">=</span> [plt.Polygon(<span class="pl-v">self</span>._faces[i, :, :<span class="pl-c1">2</span>],</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">                                  <span class="pl-vpf">facecolor</span><span class="pl-k">=</span>colors[i],</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">                                  <span class="pl-vpf">alpha</span><span class="pl-k">=</span>alpha)</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">                      <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-s3">range</span>(<span class="pl-c1">6</span>)]</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en">rotate</span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">v</span>, <span class="pl-vpf">theta</span>):</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">        new_rot <span class="pl-k">=</span> Quaternion.from_v_theta(v, theta)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">        <span class="pl-v">self</span>.current_rotation <span class="pl-k">=</span> <span class="pl-v">self</span>.current_rotation <span class="pl-k">*</span> new_rot</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">        faces_proj <span class="pl-k">=</span> project_points(<span class="pl-v">self</span>._faces, <span class="pl-v">self</span>.current_rotation,</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">                                    <span class="pl-v">self</span>.view)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">        xy <span class="pl-k">=</span> faces_proj[:, :, :<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">        zorder <span class="pl-k">=</span> <span class="pl-k">-</span>faces_proj[:, :<span class="pl-c1">4</span>, <span class="pl-c1">2</span>].mean(<span class="pl-k">-</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-s3">range</span>(<span class="pl-c1">6</span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">            <span class="pl-v">self</span>.polys[i].set_xy(xy[i])</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">            <span class="pl-v">self</span>.polys[i].set_zorder(zorder[i])</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en">set_view</span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">view</span>):</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">        <span class="pl-v">self</span>.view <span class="pl-k">=</span> view</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">        <span class="pl-v">self</span>.rotate(<span class="pl-v">self</span>.z, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en">add_to_ax</span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">ax</span>):</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">        <span class="pl-k">for</span> poly <span class="pl-k">in</span> <span class="pl-v">self</span>.polys:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">            ax.add_patch(poly)</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">        ax.set_xlim(<span class="pl-k">-</span><span class="pl-c1">3</span>, <span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">        ax.set_ylim(<span class="pl-k">-</span><span class="pl-c1">3</span>, <span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line"><span class="pl-k">if</span> <span class="pl-sv">__name__</span> <span class="pl-k">==</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">    fig, ax <span class="pl-k">=</span> plt.subplots(<span class="pl-vpf">figsize</span><span class="pl-k">=</span>(<span class="pl-c1">6</span>, <span class="pl-c1">6</span>),</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">                           <span class="pl-vpf">subplot_kw</span><span class="pl-k">=</span><span class="pl-s3">dict</span>(<span class="pl-vpf">xticks</span><span class="pl-k">=</span>[], <span class="pl-vpf">yticks</span><span class="pl-k">=</span>[]))</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">    ax.set_xlim(<span class="pl-k">-</span><span class="pl-c1">3</span>, <span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">    ax.set_ylim(<span class="pl-k">-</span><span class="pl-c1">3</span>, <span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">    c <span class="pl-k">=</span> Cube()</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">    c.add_to_ax(ax)</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">    c.rotate((<span class="pl-c1">1</span>, <span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">0</span>), <span class="pl-k">-</span>np.pi <span class="pl-k">/</span> <span class="pl-c1">6</span>)</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">    plt.show()</td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.07446s from github-fe142-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-153d6254b838872c8db73c8bd92905913f6f5b2164b7e40e5292286bd5a39403.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-f4947a80dc89b7b7941d65654d67ea6d87fb3f3baf28a2975462979455f8dcbe.js" type="text/javascript"></script>
      
      
  </body>
</html>

