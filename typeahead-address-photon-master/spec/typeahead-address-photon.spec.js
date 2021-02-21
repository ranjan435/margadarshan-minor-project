var jsdom = require('jsdom'),
    jasmineHttpServerSpy = require('jasmine-http-server-spy'),
    jasmine_expect = require('jasmine-expect');

describe('typeahead-address-photon suite', function () {

  var $,
      PhotonAddressEngine,
      httpSpy;

  beforeAll(function loadScripts(done) {
    jsdom.env({
      html: '<html><body></body></html>',
      scripts: [ 'node_modules/jquery/dist/jquery.js',
                 'node_modules/corejs-typeahead/dist/typeahead.bundle.js',
                 'src/typeahead-address-photon.js' ],
      done: function (err, window) {
        if (err) {
          console.err(err);
        }

        $ = window.$;
        PhotonAddressEngine = window.PhotonAddressEngine;

        done();
      }
    });
  });

  beforeAll(function startupMockServer(done) {
    httpSpy = jasmineHttpServerSpy.createSpyObj('mockServer', [{
      method: 'get',
      url: '/api/',
      handlerName: 'getSuggestions'
    }, {
      method: 'get',
      url: '/reverse',
      handlerName: 'getReverse'
    }]);
    httpSpy.server.start(8082, done);
  });

  afterAll(function shutdownMockServer(done) {
    httpSpy.server.stop();
    done();
    process.exit();   // hack to stop Express server
  })

  afterEach(function resetMockServer() {
    httpSpy.getSuggestions.calls.reset();
  });

  it('Test default formatType function', function () {

    // Given
    var engine = new PhotonAddressEngine(),
        feature = {
         'geometry':{
            'coordinates':[
               4.713735,
               46.4800832
            ],
            'type':'Point'
         },
         'type':'Feature',
         'properties':{
            'osm_id':409086463,
            'osm_type':'W',
            'extent':[
               4.7116237,
               46.4819855,
               4.7158754,
               46.477929
            ],
            'country':'France',
            'osm_key':'highway',
            'city':'Cortambert',
            'osm_value':'unclassified',
            'postcode':'71250',
            'name':'Voie Communale n°5 de Cluny à Cortambert',
            'state':'Bourgogne-Franche-Comté'
         }
      };

    // when
    var formattedType = engine.__testonly__.defaultFormatType(feature);

    // Then
    expect(formattedType).toBe('unclassified');
  });

  it('Test default formatResult function', function () {

    // Given
    var engine = new PhotonAddressEngine(),
        feature = {
         'geometry':{
            'coordinates':[
               4.713735,
               46.4800832
            ],
            'type':'Point'
         },
         'type':'Feature',
         'properties':{
            'osm_id':409086463,
            'osm_type':'W',
            'extent':[
               4.7116237,
               46.4819855,
               4.7158754,
               46.477929
            ],
            'country':'France',
            'osm_key':'highway',
            'city':'Cortambert',
            'osm_value':'unclassified',
            'postcode':'71250',
            'name':'Voie Communale n°5 de Cluny à Cortambert',
            'state':'Bourgogne-Franche-Comté'
         }
      };

    // When
    var formattedFeature = engine.__testonly__.defaultFormatResult(feature);

    // Then
    expect(formattedFeature).toBe('Voie Communale n°5 de Cluny à Cortambert, unclassified, Cortambert, France');
  });

  it('Test basic query', function (done) {

    // Given
    var engine = new PhotonAddressEngine({
          url: 'http://localhost:8082'
        }),
        asyncHandlerCalled = $.Deferred(),
        predictionsEventFired = $.Deferred(),
        response = {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "coordinates": [
                  13.438596,
                  52.519854
                ],
                "type": "Point"
              },
              "properties": {
                "city": "Berlin",
                "country": "Germany",
                "name": "Berlin"
              }
            },{
            "type": "Feature",
              "geometry": {
                "coordinates": [
                  61.195088,
                  54.005826
                ],
                "type": "Point"
              },
              "properties": {
                "country": "Russia",
                "name": "Berlin",
                "postcode": "457130"
              }
            }
          ]
        };

    httpSpy.getSuggestions.and.returnValue({
      statusCode: 200,
      body: response
    });

    // When
    $(engine).bind('addresspicker:predictions', function (event, predictions) {
      predictionsEventFired.resolve(predictions);
    });

    engine.ttAdapter()(
      'berlin',
      function sync(syncResults) {},
      asyncHandlerCalled.resolve);

    // Then
    $.when(asyncHandlerCalled, predictionsEventFired)
      .then(function (res1, res2) {
        expect(httpSpy.getSuggestions).toHaveBeenCalledWith(
          jasmine.objectContaining({
            query: {
              limit: '5',
              q: 'berlin'
            }
          }));

        expect(res1).toEqual(res2);

        expect(res1).toBeArrayOfSize(2);
        expect(res1).toBeArrayOfObjects();
        expect(res1[0].description).toBe('Berlin, Germany');
        expect(res1[1].description).toBe('Berlin, Russia');

        done();
      });
  });

  it('Test query with all parameters', function (done) {

    // Given
    var engine = new PhotonAddressEngine({
          url: 'http://localhost:8082',
          limit: 42,
          lat: 48.847547,
          lon: 2.351074,
          lang: 'fr',
          formatResult: function (feature) {
            return 'City of ' + feature.properties.name + ' in '
              + feature.properties.country;
          }
        }),
        response = {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "coordinates": [
                  13.438596,
                  52.519854
                ],
                "type": "Point"
              },
              "properties": {
                "city": "Berlin",
                "country": "Germany",
                "name": "Berlin"
              }
            },{
            "type": "Feature",
              "geometry": {
                "coordinates": [
                  61.195088,
                  54.005826
                ],
                "type": "Point"
              },
              "properties": {
                "country": "Russia",
                "name": "Berlin",
                "postcode": "457130"
              }
            }
          ]
        };

        httpSpy.getSuggestions.and.returnValue({
          statusCode: 200,
          body: response
        });

        // When
        engine.ttAdapter()(
          'berlin',
          function sync(syncResults) {},
          function async(asyncResults) {

            // Then
            expect(httpSpy.getSuggestions).toHaveBeenCalledWith(
              jasmine.objectContaining({
                query: {
                  q: 'berlin',
                  limit: '42',
                  lat: '48.847547',
                  lon: '2.351074',
                  lang: 'fr'
                }
              }));

            expect(asyncResults).toBeArrayOfSize(2);
            expect(asyncResults).toBeArrayOfObjects();
            expect(asyncResults[0].description).toBe('City of Berlin in Germany');
            expect(asyncResults[1].description).toBe('City of Berlin in Russia');

            done();
          });
  });

  it('Test reverse geocoding', function (done) {

    // Given
    var engine = new PhotonAddressEngine({
          url: 'http://localhost:8082'
        }),
        response = {
          'features':[
            {
              'geometry':{
                'coordinates':[
                  2.292699793534485,
                  48.8629589
                ],
                'type':'Point'
              },
              'type':'Feature',
              'properties':{
                'osm_id':1191380,
                'osm_type':'R',
                'extent':[
                  2.2924314,
                  48.8631915,
                  2.2931421,
                  48.8627112
                ],
                'country':'France',
                'osm_key':'building',
                'housenumber':'2',
                'city':'Paris',
                'street':'Avenue d\'Iéna',
                'osm_value':'yes',
                'postcode':'75116',
                'name':'Centre culturel Coréen',
                'state':'Île-de-France'
              }
            },
            {
              'geometry':{
                'coordinates':[
                  2.2926042,
                  48.8630519
                ],
                'type':'Point'
              },
              'type':'Feature',
              'properties':{
                'osm_id':938888191,
                'osm_type':'N',
                'country':'France',
                'osm_key':'place',
                'housenumber':'2',
                'city':'Paris',
                'street':'Avenue d\'Iéna',
                'osm_value':'house',
                'postcode':'75016;75116',
                'state':'Île-de-France'
              }
            }
          ],
          'type':'FeatureCollection'
        };

    httpSpy.getReverse.and.returnValue({
      statusCode: 200,
      body: response
    });

    // Then
    $(engine).bind('addresspicker:selected', function then(event, selected) {
      expect(selected).toBeObject();
      expect(selected).toBeNonEmptyObject();
      expect(selected.description).toBe('Centre culturel Coréen, yes, Paris, France');

      done();
    });

    // When
    engine.reverseGeocode([ 48.862869100279056, 2.292462587356568 ]);
  });
});
