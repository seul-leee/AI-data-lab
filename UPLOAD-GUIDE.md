# Upload guide

Each HTML page now includes its own styles and images. A missing assets folder will no longer hide the logo or portraits.

1. Extract the ZIP.
2. Open index.html to preview the homepage, or people.html to preview People.
3. GitHub repository > Code > Add file > Upload files.
4. Upload all nine HTML files from inside the extracted AI-Data-Lab folder. Upload the other files too if desired; CSS and images are also embedded in the HTML.
5. Commit changes to main.
6. Settings > Pages > Deploy from a branch > main > / (root) > Save.

People profile images are decorative research illustrations, not student likenesses. The About page uses the director headshot supplied by the owner. Robbie Reamer’s biography is supplied by the site owner; Mayukha Mulpuru and Michelle Fraginals have name-only profiles. For later design changes, edit site.css and re-embed its contents in each page, or ask for an updated package.

## Selected Work

Research now has Current Projects and Selected Work. selected-work.html contains seven publications, nineteen talks/workshops supplied by the site owner. References are transcribed and lightly standardized; no roles, funding amounts or presentation links were invented. Image sources and license details are in IMAGE-CREDITS.md.

DH-Workshop now links to dh-workshop.html. It displays the live original tutorial in an iframe and includes an external fallback link. The original Mobirise site must remain online. Research Funding has been removed from Selected Work.

## Structured data

English JSON-LD now identifies The AI Data Lab, founder Seul Lee, her affiliation with Florida State University, and her official FSU directory page. Final canonical URLs and sitemap require the actual public homepage URL. No example domain or invented deployment URL has been inserted.

## Live SEO configuration

Canonical homepage: https://seul-leee.github.io/AI-data-lab/
Sitemap: https://seul-leee.github.io/AI-data-lab/sitemap.xml

Upload sitemap.xml and all updated HTML files. In Google Search Console, add the URL-prefix property https://seul-leee.github.io/AI-data-lab/ and complete ownership verification. Submit sitemap.xml only after deployment. The empty project-archive.html page is not listed in the sitemap.
