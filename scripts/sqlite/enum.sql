DROP TABLE enum;
CREATE TABLE enum
(table_name text,
column_name text,
enum_key text,
enum_value text
);

INSERT INTO enum VALUE ('charset_table','zi_jing','NA','常用字字形表');
INSERT INTO enum VALUE ('charset_table','zi_jing','1','正體');
INSERT INTO enum VALUE ('charset_table','zi_jing','2','異體');
INSERT INTO enum VALUE ('charset_table','guo_zi','NA','常用國字標準字體表');
INSERT INTO enum VALUE ('charset_table','guo_zi','1','常用');
INSERT INTO enum VALUE ('charset_table','guo_zi','2','次常用');
INSERT INTO enum VALUE ('charset_table','gui_fan','NA','通用規範漢字表');
INSERT INTO enum VALUE ('charset_table','gui_fan','1','一級');
INSERT INTO enum VALUE ('charset_table','gui_fan','2','二級');
INSERT INTO enum VALUE ('charset_table','gui_fan','3','三級');
INSERT INTO enum VALUE ('charset_table','gui_fan','4','腳註');
COMMIT;