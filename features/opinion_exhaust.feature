Feature: Check Whether news page for blavity Website Blavity.com is appropriate

  Scenario: To check whether News page is as required
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether number of articles in opinion section are appropriate or not
      Then close the browser