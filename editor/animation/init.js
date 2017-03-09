requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'stripedWords',
                python: 'checkio'
            },
            animation: function($expl, data) {
                var checkioInput = data.in;
                if (!checkioInput){
                    return;
                }
                var vowels = "aeiouyAEIOUY";
                var consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

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
