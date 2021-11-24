Feature: Check Whether Politics page for blavity Website Blavity.com is appropriate

  Scenario: To check whether Politics page is as required
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether Politics page is as required
      Then verify footer section is present and displayed
      Then close the browser
