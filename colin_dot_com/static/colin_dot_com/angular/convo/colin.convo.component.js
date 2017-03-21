/**
 * Created by admin on 2/18/17.
 */
/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.convo').component('convo', {
    templateUrl: '/static/colin_dot_com/angular/convo/colin.convo.template.html',
    controller: ['$rootScope', '$scope', '$http', '$timeout', 'Conversation',
        function ConvoListController($rootScope, $scope, $http, $timeout, Conversation) {
            var vm = this;
            vm.items = [];
            vm.subject = "";
            vm.body = "";

            $scope.$on("convo:changed", function (event, data) {
                vm.setItems();
                vm.clearCompose();
            });

            vm.setItems = function () {
                vm.items = Conversation.get({convoId: Conversation.get_selected().friend_id}, function() {
                    var subject = vm.items[0].subject;
                    if (subject) {
                        vm.subject = !subject.startsWith("RE:") ? "RE: " + subject : subject;
                    }
                });

            }

            vm.getNewItems = function(id) {
                vm.items = Conversation.get({convoId: Conversation.get_selected().thread_id},
                    {'latest': id});
                console.log(newItems);
                for(var i = 0; i < newItems.length; i++) {
                    vm.items.push(newItems[i]);
                }
            }

            vm.clearCompose = function() {
                vm.subject = "";
                vm.body = "";
                vm.attachments = [];
            }

            vm.sendMessage = function() {
                var convo = Conversation.get_selected();
                console.log(vm.items);
                var reply_to = vm.items[vm.items.length - 1].id;
                console.log(vm);
                $.post('/api/send_message/?in_reply_to=' + reply_to, {
                    'subject': vm.subject,
                    'body': vm.body,
                    'recipient': convo.friend_id,
                    'attachmentIds': vm.attachments
                }, function(a) {
                    vm.setItems();
                    $rootScope.$broadcast("convo:new_message");
                    vm.clearCompose();
                })
            }

            vm.read = function(isVisible, msg, delay) {
                if (isVisible && msg.direction == "received" && msg.read == false) {
                    setTimeout(function() {
                        $.post('/api/read_message/?id=' + msg.id, {}, function(a) {
                            vm.items.forEach(function(item) {
                                if (item.id === msg.id) {
                                   item.read = true;
                                   
                               }
                            });
                        });
                    }, delay);
                }
            }

            vm.getFileName = function(attachment) {
                console.log(attachment);
                var str = attachment;
                var n = str.lastIndexOf('/');
                return str.substring(n + 1);
            }
            vm.attachments = [];
            vm.csrftoken = window.__csrf_token;



             $scope.images = {
                config: {
                  'options': {
                    'url': '/add_attachment/'
                  },
                  'eventHandlers': {
                    'error': function(file, response, xhr) {
                    },
                    'complete': function() {
                    },
                    'sending': function (file, formData, xhr) {
                    },
                    'success': function (file, response) {
                        console.log(response);
                        vm.attachments.push(response);
                    }
                  }
                }
              };

             vm.expanded = false;

             vm.toggle = function() {
                 vm.expanded = !vm.expanded;
             }

        }
    ]
});
