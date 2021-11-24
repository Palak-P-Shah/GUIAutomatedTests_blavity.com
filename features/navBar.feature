Feature: Nav Bar Functionality for blavity Website Blavity.com

  Scenario: Nav Bar functionality
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether nav bar is present and displayed
      Then verify whether all nav bar links are working
      Then verify footer section is present and displayed
     # Then close the browser

  Scenario Outline: Nav Bar functionality
      Then verifying page activities when "<slug>" value is passed

  Examples: 
       | slug |
       | megan-thee-stallion-says-she-plans-to-open-assisted-living-facilities-after-graduating-from-college     |
       | singer-nevaeh-jolie-comes-out-as-transgender-it-feels-like-im-saying-goodbye-but-im-saying-hello        |
     #  | hear-the-irony-roar-as-oj-simpson-weighs-in-on-tiger-king-that-ladys-husband-is-tiger-sashimi-right-now |
       | dawn-staley-earns-22-million-contract-becomes-highest-paid-black-head-coach-in-womens-basketball        |

