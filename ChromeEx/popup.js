document.addEventListener('DOMContentLoaded', function () {
    chrome.tabs.query({}, function (tabs) {
      const tabsList = document.getElementById('tabs-list');
      tabs.forEach(tab => {
        const listItem = document.createElement('li');
        listItem.textContent = tab.title + ' - ' + tab.url;
        tabsList.appendChild(listItem);
      });
    });
  });