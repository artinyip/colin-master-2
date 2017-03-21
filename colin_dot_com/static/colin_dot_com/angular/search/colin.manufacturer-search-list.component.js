/**
 * Created by admin on 11/7/16.
 */

angular.
  module('colin.search').
  component('mfgSearchList', {
    templateUrl: '/static/colin_dot_com/angular/search/colin.manufacturer-search-list.template.html',
    controller: ['$scope', '$timeout', 'SearchTerm', 'Manufacturer',
      function ManufacturerSearchListController($scope, $timeout, SearchTerm, Manufacturer) {
          var vm = this;
          vm.results = [];


          $scope.$on("searchTerm:changed", function(event, data) {
              vm.page = 0;
              vm.setResults();
          });

          vm.get_image = function(company) {
              if (!company.fields.default_image) {
                  return "";
              }
              return static_media(company.fields.default_image);
          }

          vm.shouldClear = function(index) {
              var clear = ((index + 1) % 3) === 0;
              console.log(clear);
              return clear;
          }

          vm.setResults = function() {
              vm.results = Manufacturer.query(
                  {
                      term: SearchTerm.get(),
                      company_name: SearchTerm.get()
                  });
          }

          vm.page = 0;
          vm.setResults();


      }
    ]
  });
