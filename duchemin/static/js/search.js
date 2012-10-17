var qs_map = function() {
    qs_arr = window.location.search.replace("?", '').split("&");
    qs_dict = {};
    for (var i = qs_arr.length - 1; i >= 0; i--) {
        x = qs_arr[i].split("=");
        qs_dict[x[0]] = x[1];
    }
    return qs_dict;
};

var fetchWorkResults = function() {
    console.log("Fetch work results");
    searchPageCallback('work', 1, '#works');
};

var fetchElementResults = function() {
    console.log("Fetch element results");
    searchPageCallback('element', 1, '#elements');
};

var searchPageCallback = function(searchtype, page, target) {
    console.log("Search callback for page " + page);
    qsm = qs_map();
    if (searchtype == 'work') {
        if (qsm['wpage'] === undefined) {
            qsm['wpage'] = page;
        }
    } else if (searchtype == 'element') {
        if (qsm['epage'] === undefined) {
            qsm['epage'] = page;
        }
    }
    qstr = jQuery.param(qsm);
    console.log(qsm);

    $.ajax({
        url: '/search/results/' + searchtype,
        data: qstr,
        success: function(data) {
            $(target).empty();
            $(target).append(data);
        }
    });
};

var worksPagerActions = function() {
    $('.works-next, .works-prev').on({
        'click': function(event) {
            searchPageCallback('work', $(this).attr('target'), '#works');
            return false;
        }
    });
};

var elementsPagerActions = function() {
    $('.elements-next, .elements-prev').on({
        'click': function(event) {
            searchPageCallback('element', $(this).attr('target'), '#elements');
            return false;
        }
    });
};