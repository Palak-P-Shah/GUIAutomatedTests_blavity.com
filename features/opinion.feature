Feature: Check Whether opinion page for blavity Website Blavity.com is appropriate

  Scenario: To check whether Op-Eds page is as required
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether Op-Eds page is as required
      Then verify footer section is present and displayed
      Then close the browser