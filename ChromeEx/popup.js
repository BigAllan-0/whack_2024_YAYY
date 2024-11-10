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
      let categorizedTabs = [];
      let categories = [];
  
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

        // Add categorized tab data to the array
        categorizedTabs.push({
          title: tab.title,
          url: tab.url,
          category: category
        });

        // Add the category value to the categories array
        categories.push(category);
  
        // Create list item with category info
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${tab.title}</strong> - <a href="${tab.url}" target="_blank">${tab.url}</a> 
                              <span style="color: ${category === 'Distracting' ? 'red' : 'green'}">(${category})</span>`;
        tabsList.appendChild(listItem);
      });

      let updatedCategories = categories.map(value => {
        if (value === 'Neutral') return 1;
        if (value === 'Distracting') return 2;
        if (value === 'Non-distracting') return 0;
        return value; // in case there are unexpected values
      });
      
      console.log(updatedCategories);

      // // Log the categories array to check the stored categories
      // console.log('Categories:', categories);

      // Send the categorized tabs data to the local server
      fetch('http://localhost:3000/receive-tabs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          categorizedTabs: categorizedTabs,  // Send the full tab data
          categories: updatedCategories             // Send the categories array
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Data successfully sent to server:', data);
      })
      .catch(error => console.error('Error sending data to server:', error));
    });
  });
  