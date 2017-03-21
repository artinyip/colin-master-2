/**
 * Created by admin on 11/7/16.
 */

angular.module('colin',
    [
        'colin.search',
        'colin.convo',
        'luegg.directives',
        'dropzone',
        'angular-inview'
    ]
).config(['$resourceProvider', '$httpProvider',
    function ($resourceProvider, $httpProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
}]);