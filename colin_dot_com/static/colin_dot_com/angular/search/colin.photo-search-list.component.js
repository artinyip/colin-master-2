/**
 * Created by admin on 11/7/16.
 */

angular.
  module('colin.search').
  component('photoSearchList', {
    templateUrl: '/static/colin_dot_com/angular/search/colin.photo-search-list.template.html',
    bindings: {
        company: '<',
        editMode: '<',
        details: '<',
        paged: '<',
        lightbox: '<'
    },
    controller: ['$scope', '$timeout', 'SearchTerm', 'Photo',
      function SearchListController($scope, $timeout, SearchTerm, Photo) {
          var vm = this;
          vm.results = [];

          $scope.$on("searchTerm:changed", function(event, data) {
              vm.page = 1;
              vm.setResults(function() {
                  $(document).trigger("angular-reload-masonry");
              });
          });

          vm.get_image = function(photo) {
              if (!photo.image) {
                  return "";
              }
              return static_media(photo.image);
          }

          vm.getMore = function() {
              console.log
              vm.page++;
              var more = Photo.query({
                  term: SearchTerm.get(),
                  page: vm.page,
                  company_id: vm.company
              }, function(more) {
                  for (var i = 0; i < more.length; i++) {
                      vm.results.push(more[i]);
                  }
              });

          }

          vm.setResults = function(callback) {
              vm.results = Photo.query(
                  {
                      term: SearchTerm.get(),
                      company_id: vm.company
                  }, function() {
                      callback();
                  });
              console.log(vm.results);


          }

          vm.$onInit = function() {
              vm.details = vm.details || true;
              vm.editMode = vm.editMode || true;
              vm.paged = vm.paged || false;
              vm.lightbox = vm.lightbox || false;
          }



          vm.page = 1;
          vm.setResults(function() {
              $(document).trigger("angular-setup-masonry");
          });

      }
    ]
  });
