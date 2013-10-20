

function attachAnalysisClickEvents() {
    $('.view-analysis').on({
        'click': function(event) {
            $('#analysis-modal').remove();
            modal = $("<div />", {
                "id": "analysis-modal"
            }).appendTo("body");

            $("#analysis-modal").dialog({
                'height': 500,
                'width': 920,
                'modal': true,
                'title': 'Analysis View'
            });

            ajaxRenderAnalysis($(this).attr('anid'));
            return false; // prevent the page from jumping when the link is clicked
        }
    });
}

function attachPhraseClickEvents() {
    $('.view-phrase').on({
        'click': function(event) {
            $("#analysis-modal").remove();
            var modal = $("<div />", {
                "id": "analysis-modal"
            }).appendTo("body");

            $("#analysis-modal").dialog({
                'height': 500,
                'width': 920,
                'modal': true,
                'title': 'Phrase View'
            });

            ajaxRenderPhrase($(this).attr('phid'));
            return false;
        }
    });
}

function ajaxRenderPhrase(pid) {
    $.ajax({
        url: '/data/phrase/' + pid,
        dataType: 'json',
        success: function(data, status, xhr) {
            var modal = $("#analysis-modal");

            $("<div />", {
                "id": "analysis-modal-body"
            }).appendTo(modal);

            $("#analysis-modal-body").append(data['music']);

            var MEI = $("#meiScore");
            var cv = $('div#music canvas')[0];
            render_notation(MEI, cv, data['dimensions'][0], data['dimensions'][1]);
        }
    });
}

function ajaxRenderAnalysis(anid) {
    $.ajax({
        url: '/data/analysis/' + anid,
        dataType: 'json',
        success: function(data, status, xhr) {
            var modal = $("#analysis-modal");

            $("<div />", {
                "id": "analysis-modal-body"
            }).appendTo(modal);

            $("#analysis-modal-body").append(data['music']);

            var MEI = $("#meiScore");
            var cv = $('div#music canvas')[0];
            render_notation(MEI, cv, data['dimensions'][0], data['dimensions'][1]);
        }
    });
}