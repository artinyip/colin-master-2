/**
 * Dynamic forms for colin
 *
 * @requires jQuery v1.2.6 or later
 *
 * @author John Lempka (johnlempka@gmail.com)
 *
 */
;(function($) {
    $.fn.setupDynamicForms = function() {
        var base = $(this);
        var template = $(this).html();

        add_upload_handler()

        var template_id = base.children('input').first().attr('id').replace(/^id_/, '');
        $(this).attr("form_id", template_id)

        var index = 1;

        function add_upload_handler() {
            base.parent().on('change', 'input[type=file]', function () {
                var file = $(this)[0].files[0];
                if (file) {
                    // change name of text box
                    $(this).siblings('label[for=' + $(this).attr('id') + ']').text(file.name);

                    var new_id = $(this).parent().attr("form_id");

                    if (new_id) {
                        $(this).after("<div form_id='" + new_id + "' class='close-button'>&times;</div>")
                    }
                    addInputIfNecessary();
                }
            });

            base.parent().on('click', '.close-button', function() {
                var id = $(this).attr('form_id');
                $("*[form_id=" +id +"]").remove();
                addInputIfNecessary();
            });
        }

        function addInputIfNecessary() {
            console.log("add input if nec called");
            console.log(base.parent());
            var inputs = base.parent().find('input[type=file]');
            var addAnother = true;
            console.log(inputs);
            inputs.each(function () {
                console.log($(this)[0].files);
                addAnother == addAnother && $(this)[0].files[0].length > 0;
            });
            console.log("add another? " + addAnother);
            if (addAnother == true) {
                addAnotherInput(inputs);
            }
        }

        function addAnotherInput() {
            console.log("add another called")
            var new_id = template_id.replace(/\d+/, index++);
            console.log(template)
            var new_element = base.clone();
            new_element.attr('form_id', new_id);
            var new_template = template.replace(new RegExp(template_id, "g"), new_id);
            new_element.html(new_template);

            base.parent().children(base.selector).last().after(new_element);
        }

    }

})(jQuery);
