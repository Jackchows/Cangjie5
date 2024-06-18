DROP TABLE IF EXISTS charset_table_new;
CREATE TABLE charset_table_new(
	unicode_hex		TEXT,
	u				TEXT,
	ua				TEXT,
	ub				TEXT,
	uc				TEXT,
	ud				TEXT,
	ue				TEXT,
	uf				TEXT,
	ug				TEXT,
	uh				TEXT,
	ui				TEXT,
	ci				TEXT,
	cis				TEXT,
	kr				TEXT,
	rs				TEXT,
	s				TEXT,
	sp				TEXT,
	cf				TEXT,
	idc				TEXT,
	crn				TEXT,
	pua				TEXT,
	other			TEXT,
	gb2312			TEXT,
	gbk				TEXT,
	gb18030_2022_l1	TEXT,
	gb18030_2022_l2	TEXT,
	gb18030_2022_l3	TEXT,
	big5			TEXT,
	hkscs			TEXT,
	gui_fan			TEXT,
	zi_jing			TEXT,
	guo_zi			TEXT,
	yyy				TEXT,
	zx				TEXT,
	character_value TEXT
);

CREATE INDEX "idx_charset_new_table_unicode_hex" ON "charset_table_new"("unicode_hex");
CREATE INDEX "idx_charset_new_table_u" ON "charset_table_new"("u");
CREATE INDEX "idx_charset_new_table_ua" ON "charset_table_new"("ua");
CREATE INDEX "idx_charset_new_table_ub" ON "charset_table_new"("ub");
CREATE INDEX "idx_charset_new_table_uc" ON "charset_table_new"("uc");
CREATE INDEX "idx_charset_new_table_ud" ON "charset_table_new"("ud");
CREATE INDEX "idx_charset_new_table_ue" ON "charset_table_new"("ue");
CREATE INDEX "idx_charset_new_table_uf" ON "charset_table_new"("uf");
CREATE INDEX "idx_charset_new_table_ug" ON "charset_table_new"("ug");
CREATE INDEX "idx_charset_new_table_uh" ON "charset_table_new"("uh");
CREATE INDEX "idx_charset_new_table_ui" ON "charset_table_new"("ui");
CREATE INDEX "idx_charset_new_table_ci" ON "charset_table_new"("ci");
CREATE INDEX "idx_charset_new_table_cis" ON "charset_table_new"("cis");
CREATE INDEX "idx_charset_new_table_kr" ON "charset_table_new"("kr");
CREATE INDEX "idx_charset_new_table_rs" ON "charset_table_new"("rs");
CREATE INDEX "idx_charset_new_table_s" ON "charset_table_new"("s");
CREATE INDEX "idx_charset_new_table_sp" ON "charset_table_new"("sp");
CREATE INDEX "idx_charset_new_table_cf" ON "charset_table_new"("cf");
CREATE INDEX "idx_charset_new_table_idc" ON "charset_table_new"("idc");
CREATE INDEX "idx_charset_new_table_crn" ON "charset_table_new"("crn");
CREATE INDEX "idx_charset_new_table_pua" ON "charset_table_new"("pua");
CREATE INDEX "idx_charset_new_table_other" ON "charset_table_new"("other");
CREATE INDEX "idx_charset_new_table_gb2312" ON "charset_table_new"("gb2312");
CREATE INDEX "idx_charset_new_table_gbk" ON "charset_table_new"("gbk");
CREATE INDEX "idx_charset_new_table_gb18030_2022_l1" ON "charset_table_new"("gb18030_2022_l1");
CREATE INDEX "idx_charset_new_table_gb18030_2022_l2" ON "charset_table_new"("gb18030_2022_l2");
CREATE INDEX "idx_charset_new_table_gb18030_2022_l3" ON "charset_table_new"("gb18030_2022_l3");
CREATE INDEX "idx_charset_new_table_big5" ON "charset_table_new"("big5");
CREATE INDEX "idx_charset_new_table_hkscs" ON "charset_table_new"("hkscs");
CREATE INDEX "idx_charset_new_table_gui_fan" ON "charset_table_new"("gui_fan");
CREATE INDEX "idx_charset_new_table_zi_jing" ON "charset_table_new"("zi_jing");
CREATE INDEX "idx_charset_new_table_guo_zi" ON "charset_table_new"("guo_zi");
CREATE INDEX "idx_charset_new_table_yyy" ON "charset_table_new"("yyy");
CREATE INDEX "idx_charset_new_table_zx" ON "charset_table_new"("zx");