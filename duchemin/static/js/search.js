var fetchWorkResults = function() {
    fetchInitialResults('work', 1, '#works');
};

var fetchElementResults = function() {
    fetchInitialResults('element', 1, '#elements');
};

var fetchInitialResults = function(searchtype, page, target) {
    var qstr = window.location.search.replace("?", "");
    if (searchtype == 'work') {
        if (window.location.search.match(/wpage/g) === null) {
            qstr = qstr + "&wpage=" + page;
        }
    }

    if (searchtype == 'element') {
        if (window.location.search.match(/epage/g) === null) {
            qstr = qstr + "&epage=" + page;
        }
    }

    $.ajax({
        url: '/search/results/' + searchtype,
        data: qstr,
        success: function(data) {
            $(target).empty();
            $(target).append(data);
        }
    });
}

var searchPageCallback = function(href) {
    var searchtype;
    var target;
    if (href.match('epage')) {
        searchtype = "element";
        target = "#elements";
    } else if (href.match('wpage')) {
        searchtype = "work";
        target = "#works";
    } else {
        // first time caller?
        // href = href + "&epage=1&wpage=1";
    }

    href = href.replace("?", "");

    $.ajax({
        url:'/search/results/' + searchtype,
        data: decodeURIComponent(href),
        success: function(data) {
            $(target).empty();
            $(target).append(data);
        }
    });
    // return false;
}

var attachPagerActions = function() {
    $('.pagination a').on({
        'click': function(event) {
            searchPageCallback($(this).attr('href'));
            return false;
        }
    });
};