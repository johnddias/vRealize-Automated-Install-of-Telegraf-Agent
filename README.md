# vRealize Automated Install of Telegraf Agent
 A vRealize Orchestrator package to automate the installation and configuration of Telegraf via vRealize Operations Application Monitoring for a vRealize Automation deployment.

 For more information on the structure and purpose of this workflow package please [see my blog post](https://blogs.vmware.com/management/2021/11/do-you-want-to-offer-vrealize-automation-service-broker-users-the-option-to-have-their-applications-monitored-by-vrealize-operations-automatically.html).

## Changes
25 Mar 2022 -
  * refactored to work with both vROps Cloud and On-Prem instances. Configuration element now includes a flag to determine if the request is for a vROps Cloud instance. Also added refresh token to the configuration element.
  * More robust handling of errors in installation
  * Decreased wait timer value to 60 seconds to speed up workflow (adjustable by changing the timer attribute)

## Getting Started
This solution has been developed and tested on the following products:
- vRealize Operations 8.6 (Enterprise edition required for application monitoring)
- vRealize Automation 8.6 (with embedded vRealize Orchestrator 8.6)


It may work with versions as early as 8.1, but this has not been tested. Prior versions lack the required APIs.

I see no issues with using stand-alone vRealize Orchestrator with this solution.

A trial of these products is available at VMware.com.

- [vRealize Automation (and vRealize Orchestrator)](https://www.vmware.com/products/vrealize-automation.html#get-started)
- [vRealize Operations](https://www.vmware.com/products/vrealize-operations.html)


### In vRealize Orchestrator
1. Install the vRealize Orchestrator package
  * Go to Assets > Packages
  * Click "Import"
  * Browse to and open the 'com.vmware.cmbu.tmm.telegrafInstall.package' file on your computer
  * (Optional) Click "Package elements" to view the contents of the package. All elements are required for the workflow to run, with the exception of the Resource Element, which is just the vRealize Operations icon
  * Click "Import" at the bottom of the page

2. Set up the Configuration Element
  * Go to Assets > Configurations
  * Open the web-root folder
  * Click on the vROps Telegraf Agent Install configuration element
  * Click EDIT on the top menu
  * Click the Variables tab
  * For each configuration element variable provide the values for your environment by clicking the variable and entering the value and then clicking SAVE.
    * The vROps user must have permissions to install and manage Telegraf agents
    * The OS user must have permissions as [documented in vRealize Operations 8.6 documentation](https://docs.vmware.com/en/vRealize-Operations/8.6/com.vmware.vcom.core.doc/GUID-D1152A54-550F-42AD-8B94-B83DEABCCD8C.html)
  * SAVE the configuration element changes (button is at the bottom of the screen)

3. Edit workflow for your environment
  * Go to Library > Workflows > App monitoring
  * Click the Install Telegraf Agent Workflow
  * Click edit on the workflow menu
  * Click the Schema tab
  * Click the Configure MySQL Plugin script element
  * Click the Scripting tab
  * Edit settings for the USERNAME, PASSWORD and PORT values as appropriate for your environment
  * Click the Configure Apache HTTP Plugin
  * Click the Scripting tab
  * You may not need to edit the URL value, unless you are using a different port or using https. The Apache monitoring is done using the Server Status module in Apache so that must be enabled and configured
  * Click SAVE (bottom left of screen)

### In vRealize operations
  1. [Follow the instructions in the documentation to enable OS and Application Monitoring](https://docs.vmware.com/en/vRealize-Operations/8.6/com.vmware.vcom.core.doc/GUID-D6C666EC-4073-4EBD-B5F6-A42A01712E72.html)

### In vRealize Automation
1. Configure an Event Subscription
  * In vRealize Automation - Cloud Assembly navigate to the Extensibility tab
  * Click on Subscriptions and then NEW SUBSCRIPTION
  * Name your new subscription
  * Click to add a new Event Topic
  * Select the Compute post provision topic
  * For Condition filters use `event.data.customProperties['agent']=="telegraf"`  If you do not use a condition filter, just be aware that this will trigger the workflow for each VM provisioned for any template
  * Under Action/workflow add the "Install Telegraf Agent on VM" workflow
  * SAVE the subscription

2. Add custom properties to your template
  * For each cloud template that you wish to trigger the workflow, you will need to add the custom property "agent" with a value of "telegraf"
  * For each VM that will run MySQL or Apache you will need to add the custom property "service" with a value of "mysql" or "apache" as appropriate. This will be used in the decision switch element to determine which plugin to configure
