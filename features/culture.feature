Feature: Check Whether Culture page for blavity Website Blavity.com is appropriate

  Scenario: To check whether Culture page is as required
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether Culture page is as required
      Then verify footer section is present and displayed
      Then close the browser
