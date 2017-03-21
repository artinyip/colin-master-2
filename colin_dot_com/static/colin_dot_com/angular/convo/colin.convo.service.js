/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.convo')
    .factory('Conversation', ['$resource', '$rootScope', function($resource, $rootScope) {
        var res = $resource('/api/conversations/:convoId', {}, {
                get: {
                    method: 'GET',
                    isArray: true
                },
                query: {
                    method: 'GET',
                    isArray: true
                },
                'send': {
                    method: 'POST',
                    url: '/api/send_message/',
                },
                'read': {
                    method: 'POST',
                    url: '/api/read_message/'
                }
            }
        );

        res.selected = {};

        res.get_selected = function() {
            return res.selected;
        }

        res.set_selected = function(convo) {
            res.selected = convo;
            $rootScope.$broadcast("convo:changed");
        }
        return res;
    }]);