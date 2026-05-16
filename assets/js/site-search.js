(function () {
  function normalizeText(value) {
    return (value || "").toString().toLowerCase().replace(/\s+/g, " ").trim();
  }

  function splitQuery(query) {
    return normalizeText(query).split(" ").filter(Boolean);
  }

  function escapeHtml(value) {
    return (value || "").toString().replace(/[&<>"']/g, function (char) {
      return {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      }[char];
    });
  }

  function scoreItem(item, terms) {
    var title = normalizeText(item.title);
    var description = normalizeText(item.description);
    var content = normalizeText(item.content);
    var score = 0;

    for (var i = 0; i < terms.length; i += 1) {
      var term = terms[i];

      if (title.indexOf(term) === -1 && description.indexOf(term) === -1 && content.indexOf(term) === -1) {
        return 0;
      }

      if (title.indexOf(term) !== -1) {
        score += 10;
      }
      if (description.indexOf(term) !== -1) {
        score += 5;
      }
      if (content.indexOf(term) !== -1) {
        score += 1;
      }
    }

    return score;
  }

  function excerpt(item, terms) {
    var content = (item.description || item.content || "").replace(/\s+/g, " ").trim();
    var normalized = normalizeText(content);
    var firstIndex = -1;

    for (var i = 0; i < terms.length; i += 1) {
      var index = normalized.indexOf(terms[i]);
      if (index !== -1 && (firstIndex === -1 || index < firstIndex)) {
        firstIndex = index;
      }
    }

    var start = firstIndex > 60 ? firstIndex - 60 : 0;
    var text = content.slice(start, start + 180);
    return (start > 0 ? "..." : "") + text + (content.length > start + 180 ? "..." : "");
  }

  function renderResults(results, terms, elements) {
    if (!terms.length) {
      elements.status.textContent = "キーワードを入力してください。";
      elements.results.innerHTML = "";
      return;
    }

    if (!results.length) {
      elements.status.textContent = "該当する記事は見つかりませんでした。";
      elements.results.innerHTML = "";
      return;
    }

    elements.status.textContent = results.length + "件見つかりました。";
    elements.results.innerHTML = results.slice(0, 30).map(function (item) {
      return [
        '<article class="site-search__result">',
        '<h2 class="site-search__result-title"><a href="' + escapeHtml(item.url) + '">' + escapeHtml(item.title) + "</a></h2>",
        '<p class="site-search__result-url">' + escapeHtml(item.url) + "</p>",
        '<p class="site-search__result-excerpt">' + escapeHtml(excerpt(item, terms)) + "</p>",
        "</article>"
      ].join("");
    }).join("");
  }

  window.addEventListener("DOMContentLoaded", function () {
    var root = document.querySelector("[data-search-root]");
    if (!root) {
      return;
    }

    var elements = {
      input: root.querySelector("[data-search-input]"),
      status: root.querySelector("[data-search-status]"),
      results: root.querySelector("[data-search-results]")
    };
    var indexUrl = root.getAttribute("data-search-index");
    var searchIndex = [];

    fetch(indexUrl)
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Search index request failed.");
        }
        return response.json();
      })
      .then(function (items) {
        searchIndex = items;
        elements.status.textContent = "キーワードを入力してください。";
      })
      .catch(function () {
        elements.status.textContent = "検索インデックスを読み込めませんでした。";
      });

    elements.input.addEventListener("input", function () {
      var terms = splitQuery(elements.input.value);
      var results = searchIndex.map(function (item) {
        return {
          item: item,
          score: scoreItem(item, terms)
        };
      }).filter(function (result) {
        return result.score > 0;
      }).sort(function (a, b) {
        return b.score - a.score || a.item.title.localeCompare(b.item.title, "ja");
      }).map(function (result) {
        return result.item;
      });

      renderResults(results, terms, elements);
    });
  });
}());
