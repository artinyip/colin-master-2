/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.search')
    .factory('Photo', ['$resource', function($resource) {
        return $resource('/photos/find/', {}, {
            'query' : {
                isArray: true,
                transformResponse: function(data) {
                    var resp = (JSON.parse(data));
                    return resp.results;
                }
            }
        });
    }]);