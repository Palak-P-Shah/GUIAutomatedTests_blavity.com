Feature: Home Page Verification for Blavity.com
 
  Scenario: Verify the different sections of the Home Page for Blavity.com
    Given url is launched
    When I am on blavity page
    Then check whether page is loaded
    #Then check whether arrow element is present
   # Then verify links from carousel works
    Then verify if ticker section exists
    Then verify ticker count and links    
    Then verify links arrow buttons and read more link work in carousel
    Then verify side bar top stories section and links
    Then verify load more stories section and links
    Then verify subscribe banner section
    Then verify lunchtable section
    Then verify blavity originals section
    Then verify op ed section
    Then verify from our other sites section
    Then verify footer of blavity site
    Then close the browser