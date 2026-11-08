# GitHub Pages upload guide

1. Extract AI-Data-Lab-final.zip. Open the extracted folder.
2. Double-click index.html to preview. Keep the assets folder and HTML files together.
3. In your existing GitHub repository, open Code > Add file > Upload files.
4. Drag the CONTENTS of the extracted folder into the upload area. Do not upload the ZIP or its outer folder.
5. Confirm index.html, about.html, current-projects.html, news-events.html, join-us.html, project-archive.html, site.css and assets are included.
6. Commit changes to main. If asked, use “Update AI Data Lab website”.
7. Open repository Settings > Pages. Source: Deploy from a branch. Branch: main. Folder: / (root). Save.
8. After deployment completes, use Visit site. Check navigation, images and all four project links.

No install, build command, theme or _config.yml is required. All page/asset links are relative, so this works at username.github.io/repository-name/.

If this repository already has index.md from a previous tutorial, remove that old homepage file after making a backup. Keep index.html as the homepage. Files uploaded under an outer folder will not become the root homepage.

## Editing

- Homepage: index.html
- People and lab introduction: about.html
- Projects and related publications/presentation: current-projects.html
- News and external resources: news-events.html
- Contact: join-us.html
- Shared design: site.css
- Images: assets/

Contact opens the visitor's email app addressed to lee.seul@outlook.com. No web form submits to an unverified Formspree inbox. To enable a hosted form later, configure a verified recipient with the form provider first.

Publication details are supplied by the site owner. Ongoing research lines are separate from the related published works and past presentation. No funding, recruitment deadline, team roster or unpublished findings have been invented.

## People page

people.html contains three undergraduate DEMO profiles. Portraits are synthetic illustrations, not real lab members; names and biographies are examples. Replace them before publishing real profiles. For each real student, replace the image with a separate file, remove its adl-demo-* class, and use the adl-real-portrait class. Update alt text to the student’s name and remove Sample profile labels. Do not assign a synthetic portrait to a real person.
