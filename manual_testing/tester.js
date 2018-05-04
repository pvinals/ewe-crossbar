var request = require('request');



//request.post(
//    'http://127.0.0.1:8082/call', {
//        json: {
//            procedure: 'com.channel.presence',
//            args: ["Hello", "args"],
//            kwargs: {"beaconId":"1023",
//                     "accuracy":"3.5"}
//        }
//    },
//    function (error, response, body) {
//        console.log("Testing http://127.0.0.1:8082/call")
//        console.log("This is tester for presence")
//        console.log(JSON.stringify(body.args[0], null, 2));
//        //console.log(response);
//        if (!error && response.statusCode == 200) {
//
//        }
//
//    }
//);

request.post(
    '"http://ewecrossbar.cluster.gsi.dit.upm.es/call"', {
        json: {
            procedure: 'com.channel.event',
            args: ["Hello", "args"],
            kwargs: {"text":"hello text",
                    "user": "pablo",
                    "channel": "telegram"}
        }
    },
    function (error, response, body) {
        console.log(JSON.stringify(body.args[0], null, 2));
        //console.log(response);
        if (!error && response.statusCode == 200) {

        }

    }
);


//request.post(
//    'http://127.0.0.1:8082/publish', {
//        json: {
//            topic: 'com.beacon.presence',
//            args: ["Hello", "args"],
//            kwargs: {"beaconId":"1023",
//                     "accuracy":"3.5"}
//        }
//    },
//    function (error, response, body) {
//        console.log("Testing http://127.0.0.1:8082/publish'")
//        console.log(body);
//        //console.log(response);
//        if (!error && response.statusCode == 200) {
//
//        }
//
//    }
//);
//
//
//request.post(
//    'http://ewetasker.cluster.gsi.dit.upm.es/test.php', {
//        json: {
//            topic: 'com.beacon.presence',
//            args: ["Hello", "args"],
//            kwargs: {"beaconId":"1023",
//                     "accuracy":"3.5"}
//        }
//    },
//    function (error, response, body) {
//        console.log("Testing http://ewetasker.cluster.gsi.dit.upm.es/test.php")
//        console.log(body);
//        //console.log(response);
//        if (!error && response.statusCode == 200) {
//
//        }
//
//    }
//);
//
//
//
//request.post(
//    'http://ewetasker.cluster.gsi.dit.upm.es/test.php', {
//        json: {"user": "admin","inputEvent":"@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>. @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/#>. @prefix ewe-presence: <http://gsi.dit.upm.es/ontologies/ewe-connected-home-presence/ns/#>.  ewe-presence:PresenceSensor rdf:type ewe-presence:PresenceDetectedAtDistance. ewe-presence:PresenceSensor ewe:sensorID '1023'. ewe-presence:PresenceSensor ewe:distance 2."}
//    },
//    function (error, response, body) {
//        console.log("Testing http://ewetasker.cluster.gsi.dit.upm.es/test.php with event")
//        console.log(body);
//        //console.log(response);
//        if (!error && response.statusCode == 200) {
//
//        }
//
//    }
//);
//http://127.0.0.1:8082/publish
//http://ewetasker.cluster.gsi.dit.upm.es/test.php