/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.search')
    .factory('SearchTerm', ['$rootScope', function($rootScope) {
        var service = {};

        service.term = ""

        service.set = function(term) {
            service.term = term;
            $rootScope.$broadcast("searchTerm:changed");
            window.__colin_search = term;
        }

        service.get = function() {
            return service.term;
        }

        return service;
    }]);