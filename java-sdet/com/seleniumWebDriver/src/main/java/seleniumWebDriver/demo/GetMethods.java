package com.automationTesting;

import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class GetMethods {
	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		
		//get(url) opens the url of the browser
		driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
		
		// getTitle(url)
		String res = driver.getTitle();
		System.out.println(res);
		
		// getcurrentUrl() - returns the URL of the page
		System.out.println(driver.getCurrentUrl());

		// getPageSource() - returns source code of the page
		System.out.println(driver.getPageSource());
		
		// getWindowHandle() - return ID of the single Browser window
		String windowID = driver.getWindowHandle();
		System.out.println(windowID);
		
		// getWindowHandles() - returns ID's of the multiple browser windows
		driver.findElement(By.linkText("OrangeHRM, Inc")).click(); // this opens new browser window
		Set<String> windowIDs = driver.getWindowHandles();
		System.out.println(windowIDs);
		
		driver.close();
		
	}
}

/* output
OrangeHRM
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
<html><head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>OrangeHRM</title>
      <link rel="icon" href="/web/dist/favicon.ico?v=1783336755185">
    <link href="/web/dist/css/chunk-vendors.css?v=1783336755185" rel="preload" as="style">
    <link href="/web/dist/css/app.css?v=1783336755185" rel="preload" as="style">
    <link href="/web/dist/js/chunk-vendors.js?v=1783336755185" rel="preload" as="script">
    <link href="/web/dist/js/app.js?v=1783336755185" rel="preload" as="script">
      <link href="/web/dist/css/chunk-vendors.css?v=1783336755185" rel="stylesheet">
    <link href="/web/dist/css/app.css?v=1783336755185" rel="stylesheet">
</head>
<body>
  <style>
    :root {
            --oxd-primary-one-color:#FF7B1D;
            --oxd-primary-font-color:#FFFFFF;
            --oxd-secondary-four-color:#76BC21;
            --oxd-secondary-font-color:#FFFFFF;
            --oxd-primary-gradient-start-color:#FF920B;
            --oxd-primary-gradient-end-color:#F35C17;
            --oxd-secondary-gradient-start-color:#FF920B;
            --oxd-secondary-gradient-end-color:#F35C17;
            --oxd-primary-one-lighten-5-color:#ff8a37;
            --oxd-primary-one-lighten-30-color:#ffd4b6;
            --oxd-primary-one-darken-5-color:#ff6c03;
            --oxd-primary-one-alpha-10-color:rgba(255, 123, 29, 0.1);
            --oxd-primary-one-alpha-15-color:rgba(255, 123, 29, 0.15);
            --oxd-primary-one-alpha-20-color:rgba(255, 123, 29, 0.2);
            --oxd-primary-one-alpha-50-color:rgba(255, 123, 29, 0.5);
            --oxd-secondary-four-lighten-5-color:#84d225;
            --oxd-secondary-four-darken-5-color:#68a61d;
            --oxd-secondary-four-alpha-10-color:rgba(118, 188, 33, 0.1);
            --oxd-secondary-four-alpha-15-color:rgba(118, 188, 33, 0.15);
            --oxd-secondary-four-alpha-20-color:rgba(118, 188, 33, 0.2);
            --oxd-secondary-four-alpha-50-color:rgba(118, 188, 33, 0.5);
        }
  </style>
    <noscript>
        <strong>
            We're sorry but orangehrm doesn't work properly without JavaScript enabled. Please enable it to continue.
        </strong>
    </noscript>

    <div id="app">
    <auth-login :token="&quot;c783d9b62551ecc50e.0bijgg9dUZGX5M7TNzH_PI_j3lOJcneeBclOBwP_fDc.pcLp-24vAuvliKCmdHSvDcCWuiLFHxCqYYQaMnaaEkCki8jDdSQJ1N-7qQ&quot;" :login-logo-src="&quot;\/web\/images\/ohrm_logo.png&quot;" :login-banner-src="&quot;\/web\/images\/ohrm_branding.png?v=1783336755185&quot;" :show-social-media="true" :is-demo-mode="true" :authenticators="[]">
    <template v-slot:footer="">
        <div class="orangehrm-copyright-wrapper">
            <oxd-text tag="p" class="orangehrm-copyright">OrangeHRM OS 5.9</oxd-text>
<oxd-text tag="p" class="orangehrm-copyright">© 2005 - 2026 <a href="http://www.orangehrm.com" target="_blank">OrangeHRM, Inc</a>. All rights reserved.</oxd-text>
        </div>
    </template>
    </auth-login>
    <oxd-toaster id="oxd-toaster_1"></oxd-toaster></div>
    <script type="text/javascript">
        window.appGlobal = {
          baseUrl: "/web/index.php",
          publicPath: "/web",
        };
    </script>
    <script src="/web/dist/js/chunk-vendors.js?v=1783336755185"></script>
    <script src="/web/dist/js/app.js?v=1783336755185"></script>


</body></html>
CED02D3CD05B5A4429A8DB4793E40144

 * */
