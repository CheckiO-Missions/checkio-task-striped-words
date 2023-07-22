requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            animation: function($expl, data) {
                var checkioInput = data.in[0];
                if (!checkioInput){
                    return;
                }
                const vowels = "aeiouyAEIOUY";
                const consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

                var text = "";

                for (var i = 0; i < checkioInput.length; i++) {
                    var l = checkioInput[i];
                    if (vowels.indexOf(l) !== -1) {
                        text += '<span class="vowel">' + l + '</span>';
                    }
                    else if (consonants.indexOf(l) !== -1){
                        text += '<span class="consonant">' + l + '</span>';
                    }
                    else {
                        text += l;
                    }
                }
                $expl.html(text);
            }
        });
        io.start();
    }
);
