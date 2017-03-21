/**
 * Created by admin on 11/7/16.
 */

angular.module('colin.search')
    .factory('Manufacturer', ['$resource', function($resource) {
        return $resource('/find/:term');
    }]);