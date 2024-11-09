// document.addEventListener('DOMContentLoaded', function () {
//     chrome.tabs.query({}, function (tabs) {
//       const tabsList = document.getElementById('tabs-list');
//       tabs.forEach(tab => {
//         const listItem = document.createElement('li');
//         listItem.textContent = tab.title + ' - ' + tab.url;
//         tabsList.appendChild(listItem);
//       });
//     });
//   });

  document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({}, function (tabs) {
      const tabsList = document.getElementById('tabs-list');
  
      tabs.forEach(tab => {
        // Categorize based on domain or keywords
        let category = 'Neutral';  // Default category
        const url = new URL(tab.url);
  
        // Define rules for categorization
        if (url.hostname.includes('google.com') || url.hostname.includes('wolfram.com')) {
          category = 'Non-distracting';
        } else if (url.hostname.includes('coolmathgames.com') || url.hostname.includes('games')) {
          category = 'Distracting';
        }
  
        // Create list item with category info
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${tab.title}</strong> - <a href="${tab.url}" target="_blank">${tab.url}</a> 
                              <span style="color: ${category === 'Distracting' ? 'red' : 'green'}">(${category})</span>`;
        tabsList.appendChild(listItem);
      });
    });
  });
  