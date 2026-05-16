# ms900_data.py

EXAM_TAG = "ms900"

EXAM_TITLE = "MS-900: Microsoft 365 Fundamentals Practice"

# You can keep adding Sections 4 through 10 right below this!
PRACTICE_DATA = {
    "Section 1: Cloud Concepts": [
        {
            "q": "Which cloud computing model provides a complete software solution that you purchase on a pay-as-you-go basis from a cloud service provider?",
            "options": ["Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Software as a Service (SaaS)", "On-premises"],
            "answer": 2,
            "explanation": "SaaS (Software as a Service) provides a complete product run and managed by the service provider, like Microsoft 365."
        },
        {
            "q": "What is the primary benefit of deploying resources to a public cloud rather than an on-premises data center?",
            "options": ["Complete control over physical hardware", "High Capital Expenditure (CapEx)", "Elasticity and scalability", "Data never leaves your local network"],
            "answer": 2,
            "explanation": "Public clouds offer elasticity (the ability to automatically add or remove resources) and scalability without needing to buy new physical hardware."
        },
        {
            "q": "Which Microsoft cloud model is Microsoft 365 primarily categorized as?",
            "options": ["IaaS", "PaaS", "SaaS", "DaaS"],
            "answer": 2,
            "explanation": "Microsoft 365 is a SaaS solution, providing ready-to-use applications like Word, Exchange, and Teams."
        },
        {
            "q": "If an organization wants to keep some highly sensitive data on their own local servers while utilizing the public cloud for web hosting, which cloud model are they using?",
            "options": ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Community Cloud"],
            "answer": 2,
            "explanation": "A hybrid cloud combines an on-premises data center (private cloud) with a public cloud."
        },
        {
            "q": "What financial model is generally associated with cloud computing instead of buying physical servers?",
            "options": ["Capital Expenditure (CapEx)", "Operational Expenditure (OpEx)", "Fixed cost model", "Sunk cost model"],
            "answer": 1,
            "explanation": "Cloud computing shifts costs from CapEx (buying hardware) to OpEx (paying monthly for what you use)."
        },
        {
            "q": "Which term describes a cloud service's ability to remain available after a hardware failure?",
            "options": ["Scalability", "Agility", "Fault tolerance", "Elasticity"],
            "answer": 2,
            "explanation": "Fault tolerance ensures that if one component fails, the service remains operational."
        },
        {
            "q": "Which of the following is an example of PaaS (Platform as a Service)?",
            "options": ["Microsoft Word", "Azure SQL Database", "A virtual machine hosted in Azure", "An on-premises Exchange server"],
            "answer": 1,
            "explanation": "Azure SQL Database is a managed platform (PaaS) where Microsoft manages the underlying infrastructure and OS."
        }
    ],
    "Section 2: Microsoft 365 Apps and Services": [
        {
            "q": "Which Microsoft 365 application is designed primarily as a hub for teamwork, combining chat, video meetings, and file storage?",
            "options": ["SharePoint Online", "Yammer (Viva Engage)", "Microsoft Teams", "Exchange Online"],
            "answer": 2,
            "explanation": "Microsoft Teams is the core hub for teamwork and collaboration in M365."
        },
        {
            "q": "You need to store your personal work documents in the cloud so you can access them from any device. Which service should you use?",
            "options": ["SharePoint Online", "OneDrive for Business", "Microsoft Lists", "Azure Files"],
            "answer": 1,
            "explanation": "OneDrive for Business is meant for personal file storage and sharing, whereas SharePoint is for team/site-level storage."
        },
        {
            "q": "Which Microsoft service provides enterprise-class email and calendaring?",
            "options": ["Exchange Online", "SharePoint Online", "Microsoft Intune", "Microsoft Entra ID"],
            "answer": 0,
            "explanation": "Exchange Online is the cloud-based email and calendaring server behind Microsoft 365."
        },
        {
            "q": "What tool in Microsoft 365 helps organizations manage and organize their work using a Kanban board style layout?",
            "options": ["Microsoft Planner", "Microsoft Word", "Microsoft Stream", "Microsoft Viva Insights"],
            "answer": 0,
            "explanation": "Microsoft Planner provides a visual, Kanban-style board to organize teamwork and tasks."
        },
        {
            "q": "Which feature ensures that multiple users can edit a Microsoft Word document at the exact same time?",
            "options": ["Version history", "Co-authoring", "AutoSave", "Track Changes"],
            "answer": 1,
            "explanation": "Co-authoring allows multiple people to work together in a document simultaneously."
        },
        {
            "q": "Which M365 application is best suited for hosting an organization-wide enterprise social network?",
            "options": ["Microsoft Teams", "Viva Engage (Yammer)", "Outlook", "SharePoint intranet"],
            "answer": 1,
            "explanation": "Viva Engage (formerly Yammer) is designed to connect leaders, communicators, and employees across the entire organization."
        },
        {
            "q": "What is the primary purpose of Microsoft Intune?",
            "options": ["To filter spam emails", "To manage devices and applications (MDM/MAM)", "To create corporate presentations", "To analyze employee productivity data"],
            "answer": 1,
            "explanation": "Microsoft Intune is a cloud-based endpoint management solution to manage user devices and mobile apps."
        }
    ],
    "Section 3: Security, Compliance, and Identity": [
        {
            "q": "Which Microsoft service is the core identity and access management solution in the cloud?",
            "options": ["Microsoft Defender", "Microsoft Purview", "Microsoft Entra ID", "Azure Virtual Network"],
            "answer": 2,
            "explanation": "Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based identity and access management service."
        },
        {
            "q": "What security methodology assumes that no user or device is trusted by default, even if they are inside the corporate network?",
            "options": ["Perimeter security", "Zero Trust", "Defense in depth", "Role-based access control"],
            "answer": 1,
            "explanation": "Zero Trust assumes breach and verifies every request as though it originates from an open network."
        },
        {
            "q": "Which feature requires users to provide a second form of verification (like a text code or app approval) to log in?",
            "options": ["Single Sign-On (SSO)", "Multi-Factor Authentication (MFA)", "Conditional Access", "Password hash synchronization"],
            "answer": 1,
            "explanation": "MFA requires two or more verification methods to authenticate a user, drastically improving security."
        },
        {
            "q": "What Microsoft 365 feature evaluates user login signals (like location or device state) to enforce access policies?",
            "options": ["Conditional Access", "Microsoft Purview", "Data Loss Prevention (DLP)", "eDiscovery"],
            "answer": 0,
            "explanation": "Conditional Access brings signals together to make decisions and enforce organizational policies automatically."
        },
        {
            "q": "Which Microsoft brand family covers compliance, data governance, and risk management solutions?",
            "options": ["Microsoft Defender", "Microsoft Intune", "Microsoft Purview", "Microsoft Sentinel"],
            "answer": 2,
            "explanation": "Microsoft Purview is the suite of data governance, risk, and compliance solutions."
        },
        {
            "q": "Which policy type should you use to prevent employees from accidentally emailing credit card numbers to external people?",
            "options": ["Conditional Access policy", "Data Loss Prevention (DLP) policy", "Retention policy", "Multi-Factor Authentication"],
            "answer": 1,
            "explanation": "DLP policies help identify, monitor, and automatically protect sensitive information across M365."
        },
        {
            "q": "What portal provides a centralized view of your organization's security posture with a quantifiable 'Secure Score'?",
            "options": ["Microsoft 365 admin center", "Microsoft Defender portal", "Microsoft Entra admin center", "Exchange admin center"],
            "answer": 1,
            "explanation": "The Microsoft Defender portal provides a unified view of your security posture and includes the Microsoft Secure Score."
        }
    ],
    "Section 4: Pricing, Licensing, and Support": [
        {
            "q": "What is the maximum number of users allowed for any Microsoft 365 'Business' plan (Basic, Standard, or Premium)?",
            "options": ["100 users", "300 users", "500 users", "Unlimited users"],
            "answer": 1,
            "explanation": "Microsoft 365 Business plans are designed for small to medium-sized businesses and are capped at 300 users. If you need more, you must move to an Enterprise (E) plan."
        },
        {
            "q": "Which Microsoft 365 subscription is specifically designed for 'Frontline Workers' who typically only need mobile or web-based access to tools?",
            "options": ["M365 E5", "M365 F-Series (F1/F3)", "M365 Business Standard", "Office 365 E3"],
            "answer": 1,
            "explanation": "The 'F' in F-Series stands for Frontline. These plans (F1, F3) are lower-cost options for workers who don't require the full desktop version of Office apps."
        },
        {
            "q": "An organization wants the highest level of security, advanced analytics with Power BI, and voice capabilities included in a single suite. Which plan should they choose?",
            "options": ["Microsoft 365 E3", "Microsoft 365 E5", "Microsoft 365 Business Premium", "Office 365 E1"],
            "answer": 1,
            "explanation": "M365 E5 is the 'everything' plan. It includes advanced security, compliance, analytics (Power BI Pro), and voice/telephony features that E3 does not."
        },
        {
            "q": "Which licensing model allows large organizations to standardize on Microsoft technology across the enterprise and often includes 'Software Assurance'?",
            "options": ["Cloud Solution Provider (CSP)", "Enterprise Agreement (EA)", "Direct Billing via Credit Card", "Retail licensing"],
            "answer": 1,
            "explanation": "Enterprise Agreements (EA) are designed for organizations with 500+ users/devices that want to standardize and receive volume discounts over a 3-year term."
        },
        {
            "q": "What does a Microsoft 'Service Level Agreement' (SLA) primarily define?",
            "options": ["The price of the subscription", "The list of features in the software", "Microsoft's commitment to service uptime and the credits provided if it isn't met", "The hardware requirements for the user's PC"],
            "answer": 2,
            "explanation": "An SLA is a formal commitment regarding the 'uptime' (availability) of a service, usually 99.9% for M365. If it falls below this, customers may be eligible for service credits."
        },
        {
            "q": "Where should a Microsoft 365 admin go to view the current status of services and check for any active outages?",
            "options": ["The Microsoft Trust Center", "The Service Health Dashboard in the M365 Admin Center", "The Azure Portal", "Microsoft.com/Support"],
            "answer": 1,
            "explanation": "The Service Health Dashboard provides real-time information about the health of your specific tenant's services (Teams, Exchange, etc.)."
        },
        {
            "q": "Which of the following describes 'Add-on' licensing in Microsoft 365?",
            "options": ["A way to buy Windows 11 separately", "A license that requires a 'Base' subscription to be present before it can be assigned", "A discount for buying more than 300 users", "Free software provided to students"],
            "answer": 1,
            "explanation": "Add-ons (like Copilot for Microsoft 365 or specific security features) cannot be purchased by themselves; they must be attached to a qualifying base license like M365 Business Standard or E3/E5."
        }
    ],
    "Section 5: Productivity and Collaboration": [
        {
            "q": "An organization needs to create a portal for the HR department to broadcast company-wide news and benefits information. Which SharePoint site type is best for this scenario?",
            "options": ["SharePoint Team site", "SharePoint Communication site", "SharePoint Hub site", "OneDrive for Business site"],
            "answer": 1,
            "explanation": "Communication sites are used to broadcast information to a wide audience (few authors, many readers), whereas Team sites are for collaboration within a specific group."
        },
        {
            "q": "Which Microsoft Viva module provides data-driven, privacy-protected insights into how work patterns affect wellbeing and productivity?",
            "options": ["Viva Learning", "Viva Connections", "Viva Insights", "Viva Topics"],
            "answer": 2,
            "explanation": "Viva Insights helps individuals and managers understand work habits (like focus time and meeting frequency) to improve productivity and prevent burnout."
        },
        {
            "q": "What is the primary purpose of Microsoft Loop components?",
            "options": ["To create a 3D virtual meeting room", "To provide portable pieces of content that stay in sync across Teams, Outlook, and Word", "To backup local hard drives to the cloud", "To manage physical hardware inventory"],
            "answer": 1,
            "explanation": "Loop components are atomic units of productivity (like tables or lists) that sync in real-time across multiple M365 apps."
        },
        {
            "q": "Where are files actually stored when they are uploaded to a standard 'Channel' within a Microsoft Team?",
            "options": ["A private folder in the uploader's OneDrive", "An Exchange Online mailbox", "A SharePoint Online Document Library", "The Azure SQL Database"],
            "answer": 2,
            "explanation": "Microsoft Teams uses SharePoint Online as the backend for file storage in Channels. Files shared in 1:1 chats, however, go to OneDrive."
        },
        {
            "q": "Which feature in Microsoft Teams allows you to collaborate with users from different organizations without requiring them to switch tenants?",
            "options": ["Standard Channels", "Private Channels", "Shared Channels (Teams Connect)", "Group Chats"],
            "answer": 2,
            "explanation": "Shared Channels allow users from different organizations to collaborate in a single channel without the 'tenant switching' friction of Guest access."
        },
        {
            "q": "Which service acts as the 'Hub for Teamwork,' bringing together chat, meetings, and integration with third-party apps and Power Platform?",
            "options": ["Microsoft Outlook", "Microsoft Teams", "Microsoft Yammer", "Microsoft Planner"],
            "answer": 1,
            "explanation": "Microsoft Teams is defined by Microsoft as the 'Hub for Teamwork' because it centralizes collaboration and integrates other services into one interface."
        },
        {
            "q": "How does Microsoft 365 Copilot primarily enhance productivity within Word and PowerPoint?",
            "options": ["By providing a firewall for the document", "By using AI to draft content, summarize long documents, and create presentations from prompts", "By automatically backing up the file to a local USB drive", "By limiting who can view the document based on geographic location"],
            "answer": 1,
            "explanation": "Copilot for Microsoft 365 uses Large Language Models (LLMs) to help users create, summarize, and transform content across the productivity suite."
        }
    ],
    "Section 6: Security, Compliance, and the Zero Trust Model": [
        {
            "q": "What are the three core principles of the Microsoft Zero Trust security model?",
            "options": [
                "Trust by default, Perimeter defense, and Manual verification",
                "Verify explicitly, Use least privileged access, and Assume breach",
                "Password complexity, Firewall isolation, and Multi-factor authentication",
                "Identify, Protect, and Recover"
            ],
            "answer": 1,
            "explanation": "Zero Trust relies on three key principles: Verify explicitly (always authenticate), Use least privileged access (limit user access), and Assume breach (minimize blast radius and segment access)."
        },
        {
            "q": "Which Microsoft 365 service allows you to apply 'Sensitivity Labels' to documents to classify and protect data based on its importance?",
            "options": ["Microsoft Defender for Endpoint", "Microsoft Purview Information Protection", "Microsoft Entra ID", "Microsoft Sentinel"],
            "answer": 1,
            "explanation": "Microsoft Purview Information Protection (formerly MIP) uses sensitivity labels to encrypt and protect documents and emails across the organization."
        },
        {
            "q": "Your company needs a solution that evaluates 'if-then' signals—such as user location or device health—before granting access to Microsoft 365 apps. Which feature should you use?",
            "options": ["Self-Service Password Reset (SSPR)", "Microsoft Entra Conditional Access", "Role-Based Access Control (RBAC)", "Privileged Identity Management (PIM)"],
            "answer": 1,
            "explanation": "Conditional Access is the 'policy engine' of Zero Trust. It uses signals to make automated access decisions, such as requiring MFA if a user logs in from an unknown location."
        },
        {
            "q": "In the 'Shared Responsibility Model' for SaaS (Software as a Service) like Microsoft 365, who is always responsible for the security of the data and user identities?",
            "options": ["Microsoft only", "The Customer only", "Both Microsoft and the Customer", "The Internet Service Provider"],
            "answer": 1,
            "explanation": "Regardless of the cloud model (IaaS, PaaS, or SaaS), the customer is always responsible for their own data, endpoints, accounts, and identity management."
        },
        {
            "q": "Which tool provides a unified security operations portal to manage alerts and hunt for threats across your Microsoft 365 environment?",
            "options": ["Microsoft 365 Admin Center", "Microsoft Defender Portal", "Microsoft Purview Compliance Portal", "Azure Service Health"],
            "answer": 1,
            "explanation": "The Microsoft Defender portal (security.microsoft.com) is the centralized hub for security teams to manage Defender for Office 365, Endpoint, and Cloud Apps."
        },
        {
            "q": "Which Microsoft Purview feature would a legal team use to search for, hold, and export electronic information for a legal case?",
            "options": ["Data Loss Prevention (DLP)", "eDiscovery", "Communication Compliance", "Insider Risk Management"],
            "answer": 1,
            "explanation": "eDiscovery is the process within Microsoft Purview used to identify and deliver electronic information (emails, documents, chats) that can be used as evidence in legal proceedings."
        },
        {
            "q": "What is the primary purpose of Microsoft Sentinel?",
            "options": [
                "To manage physical security at Microsoft data centers",
                "To provide a cloud-native SIEM (Security Information and Event Management) for intelligent security analytics",
                "To manage user passwords and biometric logins",
                "To host SharePoint communication sites"
            ],
            "answer": 1,
            "explanation": "Microsoft Sentinel is a SIEM and SOAR solution that aggregates security data from across the enterprise to provide a 'bird's-eye view' of potential threats."
        }
    ],
    "Section 7: Identity and Access Management": [
        {
            "q": "What is the primary role of Microsoft Entra ID in a cloud-first organization?",
            "options": [
                "To provide local file storage for users",
                "To act as a cloud-based identity and access management service",
                "To replace the physical firewall in the office",
                "To manage the organization's public website"
            ],
            "answer": 1,
            "explanation": "Microsoft Entra ID is the backbone of identity in Microsoft 365, managing user logins, permissions, and access to all cloud applications."
        },
        {
            "q": "Your organization has an existing on-premises Active Directory. Which tool should you use to synchronize these local identities to Microsoft Entra ID for a 'Hybrid' setup?",
            "options": ["Microsoft Entra Connect", "Azure Storage Explorer", "Microsoft Intune", "Microsoft Purview"],
            "answer": 0,
            "explanation": "Microsoft Entra Connect (and the newer Cloud Sync) is used to synchronize users, groups, and hashes from on-premises AD to the cloud."
        },
        {
            "q": "Which feature allows a user to sign in once with a single account to access multiple apps like Outlook, Salesforce, and Workday without being prompted again?",
            "options": ["Multi-Factor Authentication (MFA)", "Single Sign-On (SSO)", "Self-Service Password Reset (SSPR)", "Conditional Access"],
            "answer": 1,
            "explanation": "Single Sign-On (SSO) centralizes authentication so users only need to remember one set of credentials for all authorized applications."
        },
        {
            "q": "An administrator wants to ensure that users can only access the Finance app if they are on a 'Compliant' device and have completed an MFA challenge. What should they configure?",
            "options": ["Access Reviews", "Conditional Access Policies", "Privileged Identity Management", "Identity Protection"],
            "answer": 1,
            "explanation": "Conditional Access is the 'if-then' engine of Entra ID. It evaluates signals (device health, location) before granting or blocking access."
        },
        {
            "q": "Which service allows you to provide 'Just-in-Time' (JIT) administrative access, requiring users to request elevation and provide a justification before gaining high-level permissions?",
            "options": ["Microsoft Entra ID Protection", "Privileged Identity Management (PIM)", "Entra ID Governance", "Role-Based Access Control (RBAC)"],
            "answer": 1,
            "explanation": "PIM reduces the risk of 'permanent' admins by allowing users to be 'eligible' for a role and activating it only when needed for a limited time."
        },
        {
            "q": "Which authentication method is considered 'Passwordless' and uses biometric data or a PIN tied specifically to a local device?",
            "options": ["SMS text codes", "Windows Hello for Business", "Security Questions", "Email verification"],
            "answer": 1,
            "explanation": "Windows Hello for Business is a passwordless method that replaces passwords with strong two-factor authentication on PCs, using biometrics or a PIN."
        },
        {
            "q": "What type of identity should be used for an automated script or a cloud application that needs to authenticate to Azure resources without managing secrets or passwords?",
            "options": ["Guest User", "Managed Identity", "Global Administrator", "Hybrid User"],
            "answer": 1,
            "explanation": "Managed Identities provide an automatically managed identity in Entra ID for applications to use when connecting to resources, eliminating the need for developers to manage credentials."
        }
    ],
    "Section 8: Device Management (Intune and Autopilot)": [
        {
            "q": "Which service allows IT admins to pre-configure and reset new devices, getting them ready for productive use without needing to re-image the hardware manually?",
            "options": ["Windows Update for Business", "Windows Autopilot", "Microsoft Intune", "Microsoft Entra Connect"],
            "answer": 1,
            "explanation": "Windows Autopilot is a collection of technologies used to set up and pre-configure new devices, making them ready for use with zero-touch from IT."
        },
        {
            "q": "In a 'Bring Your Own Device' (BYOD) scenario where an employee uses a personal phone for work, which management approach allows the company to protect only the corporate apps without controlling the entire device?",
            "options": ["Mobile Device Management (MDM)", "Mobile Application Management (MAM)", "Mobile Identity Management (MIM)", "Full Device Encryption"],
            "answer": 1,
            "explanation": "MAM (Mobile Application Management) allows admins to manage and protect corporate data within specific apps (like Outlook) without needing full control over the user's personal phone."
        },
        {
            "q": "Which Microsoft solution is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM)?",
            "options": ["Microsoft Intune", "Configuration Manager", "Active Directory", "Microsoft Sentinel"],
            "answer": 0,
            "explanation": "Microsoft Intune is the primary cloud-native solution for managing devices (Windows, iOS, Android, macOS) and the apps on those devices."
        },
        {
            "q": "What is 'Co-management' in the context of Microsoft 365 device management?",
            "options": ["Using two different cloud providers to host data", "Managing the same Windows 10/11 devices using both Configuration Manager and Microsoft Intune", "Sharing admin rights between two people", "Running Windows and Linux on the same hardware"],
            "answer": 1,
            "explanation": "Co-management lets you concurrently manage Windows devices by using both Configuration Manager (on-premises) and Microsoft Intune (cloud)."
        },
        {
            "q": "An admin wants to ensure that all managed devices have a screen lock enabled and a minimum OS version before they can access corporate resources. Which Intune feature should they use?",
            "options": ["Configuration Profiles", "Compliance Policies", "App Protection Policies", "Conditional Access"],
            "answer": 1,
            "explanation": "Compliance policies define the rules and settings that a device must meet (like disk encryption or OS version) to be considered 'healthy' or 'compliant'."
        },
        {
            "q": "Which Intune action should be used if a mobile device is lost and you want to remove all corporate data but leave the user's personal photos and apps intact?",
            "options": ["Wipe", "Retire", "Delete", "Reboot"],
            "answer": 1,
            "explanation": "The 'Retire' action removes managed app data, settings, and email profiles assigned by Intune, but leaves the user's personal data on the device."
        },
        {
            "q": "Which tool provides a unified web-based console to manage all endpoints, including Intune, Autopilot, and Configuration Manager details?",
            "options": ["Microsoft 365 Admin Center", "Microsoft Intune admin center", "Azure Portal", "Microsoft Defender Portal"],
            "answer": 1,
            "explanation": "The Microsoft Intune admin center (formerly Endpoint Manager admin center) is the centralized hub for all device and app management tasks."
        }
    ],
    "Section 9: Service Lifecycle, SLAs, and Support": [
        {
            "q": "Which phase of the Microsoft service lifecycle allows a limited number of customers to test a new feature and provide feedback before it is released more broadly?",
            "options": ["Private Preview", "Public Preview", "General Availability (GA)", "Out of Support"],
            "answer": 0,
            "explanation": "Private Preview is the initial phase where a small group of customers tests features. Public Preview follows, where any customer can test it, before it finally reaches General Availability (GA)."
        },
        {
            "q": "What happens when a Microsoft 365 product reaches the 'End of Support' phase in its lifecycle?",
            "options": [
                "The product is automatically uninstalled from all devices",
                "The product continues to work but no longer receives security or feature updates",
                "Microsoft increases the price of the subscription",
                "The product is moved to the Public Preview phase"
            ],
            "answer": 1,
            "explanation": "End of Support means Microsoft no longer provides technical support, bug fixes, or security updates, which can put an organization at risk."
        },
        {
            "q": "How does Microsoft usually compensate customers if a service's uptime falls below the level guaranteed in the Service Level Agreement (SLA)?",
            "options": ["By sending a physical check", "By providing a service credit toward the next month's subscription fee", "By offering a free upgrade to an E5 plan", "By providing free hardware"],
            "answer": 1,
            "explanation": "Microsoft provides financial 'Service Credits' as a percentage of the monthly service fee if the uptime guarantee (typically 99.9%) is not met."
        },
        {
            "q": "Where should an administrator go to see upcoming changes, new features, and retired services across the entire Microsoft 365 suite?",
            "options": ["Microsoft 365 Roadmap", "The Windows Store", "Device Manager", "The local computer's Control Panel"],
            "answer": 0,
            "explanation": "The Microsoft 365 Roadmap is the official public site where anyone can track the development, rollout, and launch status of features."
        },
        {
            "q": "Which tool in the Microsoft 365 Admin Center provides a history of past service incidents and the 'Post-Incident Reviews' (PIRs) for major outages?",
            "options": ["Message Center", "Service Health Dashboard", "Security & Compliance Center", "User Settings"],
            "answer": 1,
            "explanation": "The Service Health Dashboard not only shows current status but also provides a 'History' tab where you can view details and root cause analysis of past incidents."
        },
        {
            "q": "A large enterprise requires a support plan that includes a designated Technical Account Manager (TAM) and 24/7 support for all Microsoft products. Which support level do they likely need?",
            "options": ["Basic Support", "Professional Direct", "Unified Support (or Premier)", "Community Support"],
            "answer": 2,
            "explanation": "Unified/Premier Support is the highest level of support, offering comprehensive coverage, proactive services, and dedicated technical resources for large organizations."
        },
        {
            "q": "If a service has a 99.9% uptime guarantee, what is the maximum allowed downtime per month approximately?",
            "options": ["About 8 hours", "About 43 minutes", "About 5 minutes", "24 hours"],
            "answer": 1,
            "explanation": "A 99.9% (three nines) SLA allows for roughly 43.8 minutes of downtime per month. 99.99% (four nines) allows for only about 4.4 minutes."
        }
    ],
    "Section 10: Pricing, Licensing, and Support (2026 Updates)": [
        {
            "q": "An organization with 250 employees wants a single license that includes advanced security, device management, and Microsoft 365 Copilot. Which 'Smart Bundle' is the most cost-effective recommendation?",
            "options": ["Microsoft 365 Business Basic + Copilot Add-on", "Microsoft 365 Business Premium with Copilot Business", "Office 365 E3", "Microsoft 365 F1"],
            "answer": 1,
            "explanation": "In 2026, Business Premium with the Copilot bundle is the 'strategic baseline' for SMBs, providing the security needed for responsible AI use."
        },
        {
            "q": "Which licensing model is specifically designed for large organizations (500+ users) that want to standardize on Microsoft 365 with a 3-year agreement and volume discounts?",
            "options": ["Cloud Solution Provider (CSP)", "Microsoft Customer Agreement (MCA)", "Enterprise Agreement (EA)", "Personal Subscription"],
            "answer": 2,
            "explanation": "The Enterprise Agreement (EA) is for large-scale organizations that want fixed pricing and custom terms over a multi-year period."
        },
        {
            "q": "How is usage for custom AI agents created in Microsoft Copilot Studio primarily billed in 2026?",
            "options": ["Flat monthly fee per user", "Copilot Credits (Capacity Packs or Pay-as-you-go)", "Included for free with all E5 licenses", "By the number of files stored in SharePoint"],
            "answer": 1,
            "explanation": "Copilot Studio now uses a credit-based system where organizations purchase capacity packs or use a pay-as-you-go meter for agent activity."
        },
        {
            "q": "A company has frontline staff who only use mobile devices to check email and shifts. Which license provides the best value for these 'Frontline Workers'?",
            "options": ["Microsoft 365 E5", "Microsoft 365 F1 or F3", "Microsoft 365 Business Standard", "Windows 11 Enterprise"],
            "answer": 1,
            "explanation": "The 'F' series (Frontline) licenses are designed for workers who don't have a dedicated desk and primarily use mobile/web versions of apps."
        },
        {
            "q": "Which type of support plan includes a dedicated Technical Account Manager (TAM) and advisory services for complex deployments?",
            "options": ["Basic Support", "Professional Direct", "Unified Support", "Community Support"],
            "answer": 2,
            "explanation": "Unified (formerly Premier) Support provides the highest level of human-led assistance, including a TAM and 24/7 proactive monitoring."
        },
        {
            "q": "If an organization wants to add 'Microsoft 365 Copilot' to their existing subscription, which of the following is now a qualifying base license in 2026?",
            "options": ["Microsoft 365 Business Basic", "Microsoft 365 F3", "Microsoft 365 E3", "All of the above"],
            "answer": 3,
            "explanation": "As of 2026, Microsoft has expanded Copilot eligibility to include almost all commercial plans, including Business Basic and Frontline (F) series."
        },
        {
            "q": "What is the main financial benefit of moving from on-premises servers to Microsoft 365 cloud services?",
            "options": ["Switching from OpEx to CapEx", "Switching from CapEx to OpEx", "Eliminating the need for internet connectivity", "Ensuring that data is never backed up"],
            "answer": 1,
            "explanation": "Cloud services use an Operational Expenditure (OpEx) model (pay-for-what-you-use), eliminating the large upfront Capital Expenditure (CapEx) of buying hardware."
        }
    ],
    "Section 11: Final Review Mix (The Tricky Topics)": [
        {
            "q": "In the Shared Responsibility Model, which of the following is ALWAYS the responsibility of the customer, even in a SaaS (Microsoft 365) environment?",
            "options": ["Physical security of data centers", "Data governance and user identities", "Operating system updates for the server", "Power and cooling for the hardware"],
            "answer": 1,
            "explanation": "The customer is always responsible for their own data, their users' accounts (identities), and the devices (endpoints) they use."
        },
        {
            "q": "Which Microsoft Purview feature would you use to prevent a user from accidentally sharing a Social Security Number via an email to an external recipient?",
            "options": ["Sensitivity Labels", "Data Loss Prevention (DLP)", "eDiscovery", "Insider Risk Management"],
            "answer": 1,
            "explanation": "DLP identifies, monitors, and automatically protects sensitive information (like SSNs or Credit Card numbers) across M365."
        },
        {
            "q": "What is the key difference between a Public Preview and General Availability (GA)?",
            "options": ["Public Preview is free, GA is paid", "GA is covered by a Service Level Agreement (SLA); Public Preview is not", "Public Preview is only for admins; GA is for everyone", "There is no difference"],
            "answer": 1,
            "explanation": "Features in Public Preview are for testing and usually lack an SLA or full support. GA features are production-ready and fully supported."
        },
        {
            "q": "Which service acts as a 'Cloud SIEM' (Security Information and Event Management) to aggregate logs from both Microsoft and non-Microsoft sources?",
            "options": ["Microsoft Defender for Endpoint", "Microsoft Sentinel", "Microsoft Entra ID", "Microsoft Purview"],
            "answer": 1,
            "explanation": "Sentinel is the 'big picture' tool that collects data from the entire enterprise (SIEM) and automates responses (SOAR)."
        },
        {
            "q": "Which feature of Microsoft Entra ID Protection specifically detects leaked credentials on the dark web and triggers an automatic password reset?",
            "options": ["Conditional Access", "Risk-based policies", "Multi-Factor Authentication", "Self-Service Password Reset"],
            "answer": 1,
            "explanation": "Entra ID Protection analyzes signals to identify 'User Risk' (like leaked credentials) and can enforce automated remediation via policies."
        },
        {
            "q": "A user needs to access a specific admin role for only 4 hours to complete a task. Which service should be used to provide this temporary access?",
            "options": ["Role-Based Access Control (RBAC)", "Privileged Identity Management (PIM)", "Conditional Access", "Entra ID Connect"],
            "answer": 1,
            "explanation": "PIM provides 'Just-In-Time' (JIT) access, allowing users to activate an admin role only when needed for a set duration."
        },
        {
            "q": "Which tool would an IT Admin use to view a timeline of *planned* changes to the Microsoft 365 environment, such as a new button being added to Teams next month?",
            "options": ["Service Health Dashboard", "Microsoft 365 Message Center", "Security & Compliance Center", "Azure Service Health"],
            "answer": 1,
            "explanation": "The Message Center is the primary way Microsoft communicates planned updates and changes. Service Health is for current, unplanned outages."
        }
    ]
}