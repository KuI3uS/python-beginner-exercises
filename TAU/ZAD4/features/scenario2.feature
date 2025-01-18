Feature: Anime Navigation Testing

  Scenario Outline: Validate dropdown functionality and navigate to a specific anime page using <browser> browser
    Given The user launches the website "https://www.youtube.com" via "<browser>" browser
    When The user accepts the cookie policy
    And The user hovers over the dropdown menu
    And The user clicks on a specific anime link
    Then The user should land on the correct anime page

    Examples:
      | browser  |
      | Chrome   |
      | Edge     |