/**
 * Created by johnlempka on 10/17/16.
 */


$(document).ready(function() {

    // steps
    setupCsrf();
    styleDynamicFormsets();
    searchBarButtonSetup();
    getUnreadMessages();
    setupSearchBar();
    setupLightbox();
    Dropzone.autoDiscover = false;

    // functions
    function setupCsrf() {
        var token = Cookies.get('csrftoken');
        window.__csrf_token = token;

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", token);
                }
            }
        });
    }

    function styleDynamicFormsets() {
        $(".add-row").each(function() {
            var html = $(this).html();
            $(this).html("<i class='fa fa-plus' aria-hidden=true></i> " + html);
        });
    }

    function searchBarButtonSetup() {
        $('button.search-button').on('click', function (e) {
            if (!$('.search-bar input').attr('value')) {
                e.preventDefault();
                $('.search-bar input').focus();
            }
        });
    }


    function setupSearchBar() {
        $('.search-bar-input').selectize({
            delimiter: ',',
            persist: false,
            create: function(input) {
                return {
                    value: input,
                    text: input
                }
            }
        });
    }

    function getUnreadMessages() {
        $.get('/unread_messages', function(response) {
           if (response.count > 0) {
               var li = $('.message_link');

               console.log(li);
               li.find('a').prepend("<div class='unread link'>" + response.count + "</div>");

               // var append = "<div class='message_preview'>";
               //
               // var message_list = JSON.parse(response.messages);
               //
               // for(var i = 0; i < message_list.length; i++) {
               //     var message = message_list[i]
               //     console.log(message);
               //     append += "<li>" + message.fields.subject + "</li>";
               // }
               // append+= "</ul>";
               //
               // li.append(append);
               //
               // window.setTimeout(function() {
               //     $('.message_link').foundation();
               // }, 0);
           }
        })
    }

    function setupLightbox() {
        // lightbox.option({
        //   'resizeDuration': 0,
        //   'wrapAround': true
        // })
    }


});

