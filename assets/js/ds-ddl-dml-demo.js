(() => {
  "use strict";
  const root = document.getElementById("ds-ddl-dml-demo");
  if (!root) return;

  const operations = {
    create: {kind:"DDL", sql:"CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50));",
      explain:"テーブルと列の構造を作りました。まだ行はありません。"},
    alter: {kind:"DDL", sql:"ALTER TABLE employees ADD department VARCHAR(30);",
      explain:"department列を追加しました。既存行がある場合、新しい列はこの例ではNULLになります。"},
    insert: {kind:"DML", sql:"INSERT INTO employees (id, name) VALUES (1, '佐藤');",
      explain:"employeesの中に社員データを1行追加しました。構造は変わりません。"},
    select: {kind:"DML", sql:"SELECT * FROM employees;",
      explain:"現在の行を取得しました。テーブルの構造も保存データも変化しません。"},
    update: {kind:"DML", sql:"UPDATE employees SET name = '鈴木' WHERE id = 1;",
      explain:"idが1の行のnameを鈴木に更新しました。列構造は変わりません。"},
    delete: {kind:"DML", sql:"DELETE FROM employees WHERE id = 1;",
      explain:"idが1の行だけを削除しました。テーブルと列は残ります。"},
    drop: {kind:"DDL", sql:"DROP TABLE employees;",
      explain:"テーブル自体と、その中のすべての行を削除しました。"}
  };
  const choice = root.querySelector("[data-operation]");
  const prediction = root.querySelector("[data-prediction]");
  const sql = root.querySelector("[data-sql]");
  const kind = root.querySelector("[data-kind]");
  const columns = root.querySelector("[data-columns]");
  const rowCount = root.querySelector("[data-row-count]");
  const tableHost = root.querySelector("[data-table]");
  const feedback = root.querySelector("[data-feedback]");
  const history = root.querySelector("[data-history]");
  let tableExists = false;
  let fields = [];
  let rows = [];
  let actions = [];

  function reset() {
    tableExists = false;
    fields = [];
    rows = [];
    actions = [];
    choice.value = "create";
    prediction.value = "";
    kind.textContent = "分類：実行後に表示";
    feedback.textContent = "最初はテーブルがありません。まずCREATEを実行してみましょう。";
    render();
  }

  function render() {
    const op = operations[choice.value];
    sql.textContent = op.sql;
    columns.textContent = tableExists ? fields.join(" / ") : "テーブルなし";
    rowCount.textContent = tableExists ? rows.length + "行" : "—";
    tableHost.replaceChildren();
    if (!tableExists) {
      const p = document.createElement("p");
      p.textContent = "employees テーブルは存在しません。";
      tableHost.append(p);
    } else {
      const table = document.createElement("table");
      const thead = document.createElement("thead");
      const header = document.createElement("tr");
      fields.forEach(field => {
        const th = document.createElement("th");
        th.scope = "col";
        th.textContent = field;
        header.append(th);
      });
      thead.append(header);
      table.append(thead);
      const tbody = document.createElement("tbody");
      if (rows.length === 0) {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = fields.length;
        td.textContent = "データ行はありません";
        tr.append(td);
        tbody.append(tr);
      } else {
        rows.forEach(record => {
          const tr = document.createElement("tr");
          fields.forEach(field => {
            const td = document.createElement("td");
            td.textContent = record[field] === null ? "NULL" : String(record[field]);
            tr.append(td);
          });
          tbody.append(tr);
        });
      }
      table.append(tbody);
      tableHost.append(table);
    }
    history.replaceChildren();
    if (actions.length === 0) {
      const li = document.createElement("li");
      li.textContent = "まだ実行していません。";
      history.append(li);
    } else {
      actions.forEach(entry => {
        const li = document.createElement("li");
        li.textContent = entry;
        history.append(li);
      });
    }
  }

  choice.addEventListener("change", () => {
    prediction.value = "";
    kind.textContent = "分類：実行後に表示";
    feedback.textContent = "実行前にDDLかDMLか予想してみましょう（省略できます）。";
    render();
  });

  root.querySelector("[data-execute]").addEventListener("click", () => {
    const key = choice.value;
    const op = operations[key];
    const guess = prediction.value;
    let success = true;
    let message = op.explain;

    if (key === "create") {
      if (tableExists) {success = false;message = "employees テーブルは既にあります。CREATEするなら先にDROPしてください。";}
      else {tableExists = true;fields = ["id","name"];rows = [];}
    } else if (!tableExists) {
      success = false;
      message = "employees テーブルがないため実行できません。まずCREATEしてください。";
    } else if (key === "alter") {
      if (fields.includes("department")) {success=false;message="department列は既にあります。この例では同じ列をもう一度追加できません。";}
      else {fields.push("department");rows.forEach(record=>{record.department=null;});}
    } else if (key === "insert") {
      if (rows.some(r=>r.id===1)) {success=false;message="id=1の行が既にあります。主キーが重複するため追加できません。";}
      else {const record={id:1,name:"佐藤"};if(fields.includes("department"))record.department=null;rows.push(record);}
    } else if (key === "update") {
      const record=rows.find(r=>r.id===1);
      if (!record) {message="id=1の行がないため、更新対象は0行でした。";}
      else {record.name="鈴木";}
    } else if (key === "delete") {
      const before=rows.length;
      rows=rows.filter(r=>r.id!==1);
      if (rows.length===before) message="id=1の行がないため、削除対象は0行でした。テーブルは残ります。";
    } else if (key === "drop") {
      tableExists=false;fields=[];rows=[];
    }
    kind.textContent = "分類：" + op.kind + (success ? "（実行）" : "（実行できず）");
    const result = guess ? (guess===op.kind ? "分類の予想は正解です。 " : "分類の予想を確認しましょう。 ") : "";
    feedback.textContent = result + message + (op.kind==="DDL" ? " DDLは構造を扱います。" : " DMLはデータを扱います。");
    actions.push(key.toUpperCase() + "（" + op.kind + "）：" + (success ? "実行" : "実行できず"));
    prediction.value = "";
    render();
  });

  root.querySelector("[data-reset]").addEventListener("click", reset);
  reset();
})();
