/**
 * Created by admin on 2/18/17.
 */
/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.convo').component('convoList', {
    templateUrl: '/static/colin_dot_com/angular/convo/colin.convo-list.template.html',
    controller: ['$scope', '$timeout', 'Conversation',
        function ConvoListController($scope, $timeout, Conversation) {
            var vm = this;
            vm.items = [];


            vm.set_selected = function (convo) {
                Conversation.set_selected(convo);
            }

            vm.is_selected = function (id) {
                return id === Conversation.get_selected().thread_id;
            }

            vm.setItems = function () {
                vm.items = Conversation.query({}, function() {
                    vm.set_selected(vm.items[0]);
                });
            }

            $scope.$on("convo:new_message", function(event, data) {
                vm.setItems();
            });

            vm.setItems();
        }


    ]
});
