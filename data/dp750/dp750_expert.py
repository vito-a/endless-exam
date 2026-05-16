# databricks_data_engineer_prep.py - Advanced & Expert Editions

EXAM_TAG = "dp750"

EXAM_TITLE = "Databricks Certified Data Engineer - Advanced & Expert Prep"

PRACTICE_DATA = {
    "Section 1: Advanced Databricks Data Engineering": [
        {
            "q": "In a Delta Live Tables (DLT) pipeline, you are building a Silver layer table from raw Bronze data. You must enforce a data quality rule where `order_total > 0`. If a record fails this rule, it should be excluded from the target table, but the pipeline must continue processing the remaining valid records without failing. Which expectation syntax correctly achieves this?",
            "options": [
                "@dlt.expect(\"valid_total\", \"order_total > 0\")",
                "@dlt.expect_or_drop(\"valid_total\", \"order_total > 0\")",
                "@dlt.expect_or_fail(\"valid_total\", \"order_total > 0\")",
                "@dlt.expect_all_or_drop({\"valid_total\": \"order_total > 0\"})"
            ],
            "answer": 1,
            "explanation": "The expect_or_drop() decorator correctly evaluates the condition, drops any records that fail the check, and allows the pipeline to continue processing."
        },
        {
            "q": "A data engineer is using Auto Loader (`cloudFiles`) to continuously ingest JSON telemetry data into a Delta table. The source system is unpredictable, and new files often arrive with unexpected columns not present in the initial schema. The engineering team requires the stream to explicitly halt so they can manually review any new schema changes before integrating them. Which configuration should be applied to `cloudFiles.schemaEvolutionMode`?",
            "options": [
                "addNewColumns",
                "rescue",
                "failOnNewColumns",
                "none"
            ],
            "answer": 2,
            "explanation": "This mode halts the streaming query whenever a column not present in the current schema is detected, forcing manual intervention and review."
        },
        {
            "q": "A healthcare organization uses Unity Catalog. They have a `patients` table containing sensitive Personal Identifiable Information (PII). Only users assigned to the Unity Catalog group `pii_admins` should see the actual data in the `ssn` column. All other users should see a masked string: `'***-**-****'`. What is the most architecturally sound way to implement this column-level security?",
            "options": [
                "Create a dynamic view using `CASE WHEN is_account_group_member('pii_admins') THEN ssn ELSE '***-**-****' END`.",
                "Use the SQL command: `GRANT UNMASK ON COLUMN ssn TO pii_admins`.",
                "Apply a row filter on the table using the `current_user()` function.",
                "Create a separate Delta table for non-admins that physically omits the column, and use `REVOKE SELECT` on the original table."
            ],
            "answer": 0,
            "explanation": "Dynamic views leveraging Unity Catalog's built-in group membership functions are the standard and most secure way to apply column-level masking without duplicating data."
        },
        {
            "q": "Given a PySpark DataFrame `purchases_df` with columns `customer_id`, `purchase_date`, and `amount`, a data engineer needs to extract the row representing the *second highest* purchase amount for each customer. Which code snippet correctly uses PySpark window functions to accomplish this?",
            "options": [
                "windowSpec = Window.partitionBy(\"amount\").orderBy(col(\"customer_id\").desc())\\npurchases_df.withColumn(\"rank\", dense_rank().over(windowSpec)).filter(col(\"rank\") == 2)",
                "purchases_df.groupBy(\"customer_id\").agg(max(\"amount\").alias(\"max_amt\")).withColumn(\"rank\", rank().over(Window.orderBy(\"max_amt\"))).filter(col(\"rank\") == 2)",
                "windowSpec = Window.partitionBy(\"customer_id\").orderBy(col(\"amount\").desc())\\npurchases_df.withColumn(\"rank\", dense_rank().over(windowSpec)).filter(col(\"rank\") == 2)",
                "windowSpec = Window.partitionBy(\"customer_id\").orderBy(\"purchase_date\")\\npurchases_df.withColumn(\"rank\", row_number().over(windowSpec)).filter(col(\"rank\") == 2)"
            ],
            "answer": 2,
            "explanation": "This correctly groups the data by customer_id and orders their purchases from highest to lowest amount. dense_rank() ensures that if the top two amounts are identical, the true second-highest value is still captured as rank 2."
        },
        {
            "q": "A data engineer is applying Change Data Capture (CDC) events from a source transactional database to a target Delta table. The incoming CDC DataFrame `updates_df` has an `operation` column containing 'INSERT', 'UPDATE', or 'DELETE'. Which `MERGE INTO` statement correctly processes all three operation types?",
            "options": [
                "MERGE INTO target t USING updates_df s ON t.id = s.id\\nWHEN MATCHED THEN UPDATE SET *\\nWHEN NOT MATCHED THEN INSERT *",
                "UPSERT INTO target t USING updates_df s ON t.id = s.id\\nWITH DELETE WHERE s.operation = 'DELETE'",
                "MERGE INTO target t USING updates_df s ON t.id = s.id\\nWHEN MATCHED AND s.operation = 'DELETE' THEN DELETE\\nWHEN MATCHED AND s.operation = 'UPDATE' THEN UPDATE SET *\\nWHEN NOT MATCHED AND s.operation = 'INSERT' THEN INSERT *",
                "MERGE INTO target t USING updates_df s ON t.id = s.id\\nWHEN MATCHED THEN DELETE WHERE s.operation = 'DELETE'\\nWHEN MATCHED THEN UPDATE SET *\\nWHEN NOT MATCHED THEN INSERT *"
            ],
            "answer": 2,
            "explanation": "Delta Lake allows multiple WHEN MATCHED clauses provided they have distinct secondary conditions. This perfectly maps the CDC operation types to the target table actions."
        },
        {
            "q": "A table named `sensor_data` contains billions of rows partitioned by `date`. Analysts frequently query this table filtering by both `date` and a high-cardinality `device_id` column. Queries are extremely slow because files within each daily partition are large and disorganized. Which Databricks optimization technique will most efficiently speed up queries searching for a specific `device_id`?",
            "options": [
                "Re-partition the table by both `date` and `device_id`.",
                "Run `VACUUM sensor_data RETAIN 0 HOURS`.",
                "Use `CACHE TABLE sensor_data` before running queries.",
                "Run `OPTIMIZE sensor_data ZORDER BY (device_id)`."
            ],
            "answer": 3,
            "explanation": "Z-Ordering colocalizes related information (like a specific device_id) into the same set of files within existing partitions. This allows Databricks to use data skipping effectively and vastly improves read performance on high-cardinality columns."
        },
        {
            "q": "In a Databricks Workflow consisting of multiple tasks, 'Task_A' (a Python notebook) calculates a dynamic watermark timestamp based on data anomalies. 'Task_B' needs to use this exact timestamp to filter incoming streaming data. How can the data engineer natively pass this scalar value from 'Task_A' to 'Task_B' without writing to storage?",
            "options": [
                "Define a cluster-scoped environment variable `WATERMARK_TS` in Task A using `os.environ`.",
                "Use `dbutils.jobs.taskValues.set()` in Task A, and `dbutils.jobs.taskValues.get()` in Task B.",
                "Save the value to a temporary Delta table in Task A and read it back via PySpark in Task B.",
                "Use the Databricks REST API within Task A to update Task B's parameters at runtime."
            ],
            "answer": 1,
            "explanation": "The taskValues API is explicitly designed for passing context, metadata, and small variables (up to 48MB) between tasks within a Databricks Workflow."
        },
        {
            "q": "A junior analyst accidentally executed `DELETE FROM customers WHERE region = 'EMEA'`. A data engineer attempts to restore the table using Delta Time Travel: `RESTORE TABLE customers TO VERSION AS OF 15`. However, the command throws an error and fails to restore the data. What is the most likely reason for this failure?",
            "options": [
                "Time Travel is only supported for undoing `UPDATE` and `MERGE` operations, not `DELETE`.",
                "The transaction log (`_delta_log`) has been automatically truncated, preventing access to version 15.",
                "The user attempting the `RESTORE` command must be an admin, regardless of table ownership.",
                "The `VACUUM` command was recently executed on the table with a retention period that removed the data files associated with version 15."
            ],
            "answer": 3,
            "explanation": "Time travel relies on the physical Parquet data files of previous versions. If VACUUM permanently deletes those unreferenced files, you can no longer travel back to a version that requires them."
        },
        {
            "q": "A Spark Structured Streaming application calculates a 10-minute tumbling window average of server CPU usage. Some servers process batch jobs that cause their telemetry data to arrive with a slight delay. To prevent the aggregation state from growing infinitely while accommodating telemetry data that is up to 5 minutes late, which PySpark DataFrame method must be applied before the `.groupBy()`?",
            "options": [
                ".trigger(processingTime=\"5 minutes\")",
                ".option(\"maxLateArrivals\", \"5m\")",
                ".withWatermark(\"timestamp\", \"5 minutes\")",
                ".expireStateAfter(\"5 minutes\")"
            ],
            "answer": 2,
            "explanation": "Watermarking explicitly defines how long the system waits for late data (based on event time) before finalizing the window and dropping the state from memory."
        },
        {
            "q": "When configuring access to an AWS S3 bucket or Azure Data Lake Storage Gen2 container within Unity Catalog, what is the architectural relationship between a 'Storage Credential' and an 'External Location'?",
            "options": [
                "An External Location defines the IAM role or Service Principal, while a Storage Credential points to the specific S3 URI or ADLS path.",
                "They are synonymous concepts and can be used interchangeably when creating external tables.",
                "A Storage Credential encapsulates the authentication entity (e.g., IAM role), and an External Location combines this credential with a specific cloud storage path to govern access.",
                "A Storage Credential is used exclusively for reading data, while an External Location is required for writing data."
            ],
            "answer": 2,
            "explanation": "This accurately describes the Unity Catalog model: you create a Storage Credential to hold the keys/roles, and then map an External Location (a specific bucket path) to that credential."
        }
    ],
    "Section 2: Expert Databricks Data Engineering": [
        {
            "q": "In a Delta Live Tables (DLT) pipeline, you are implementing a Slowly Changing Dimension Type 2 (SCD Type 2) table to track historical changes to customer addresses. Which `APPLY CHANGES INTO` configuration is required to ensure that historical versions of a record are preserved rather than overwritten?",
            "options": [
                "STORED AS SCD TYPE 2",
                "SEQUENCE_BY timestamp",
                "TRACK HISTORY ON (address)",
                "SET delta.enableChangeDataFeed = true"
            ],
            "answer": 0,
            "explanation": "The `STORED AS SCD TYPE 2` clause is specifically designed to manage the valid-from and valid-to timestamps and the current-flag logic required for historical tracking in DLT."
        },
        {
            "q": "A Data Engineer drops a Unity Catalog **External Table** using the command `DROP TABLE main.staged_data.logs`. A week later, they realize the data is still needed. What is the status of the underlying data files in the cloud storage (S3/ADLS)?",
            "options": [
                "The data files are intact and can be re-registered by creating a new table pointing to the same location.",
                "The data files were moved to the Unity Catalog 'Trash' and can be recovered within 30 days.",
                "The data files were deleted because the Storage Credential had 'DELETE' permissions.",
                "The data files were deleted, but can be recovered using Delta Time Travel on the underlying path."
            ],
            "answer": 0,
            "explanation": "Dropping an External Table in Unity Catalog only removes the metadata from the catalog; the physical data files remain in the cloud storage bucket."
        },
        {
            "q": "You are querying a Delta table with Change Data Feed (CDF) enabled. You need to see only the records that were *updated*, including both the values before the update and the values after. Which value in the `_change_type` column should you filter for?",
            "options": [
                "update_preimage and update_postimage",
                "update",
                "insert and delete",
                "row_changed"
            ],
            "answer": 0,
            "explanation": "CDF generates two rows for every update: the 'preimage' contains the data before the change, and the 'postimage' contains the data after the change."
        },
        {
            "q": "When using Auto Loader, you want to force a specific column `user_id` to always be treated as a `STRING`, even if the source JSON files contain it as an integer. Which configuration allows this without defining the entire schema?",
            "options": [
                "cloudFiles.schemaHints",
                "cloudFiles.inferSchema",
                "cloudFiles.schemaEvolutionMode",
                "spark.sql.columnNameOfCorruptRecord"
            ],
            "answer": 0,
            "explanation": "`schemaHints` allows you to provide a partial schema to override specific columns while still letting Auto Loader infer the rest of the schema dynamically."
        },
        {
            "q": "A Structured Streaming job using a `groupBy().avg()` aggregation is failing with an `OutOfMemoryError` on the executors. The watermark is set correctly. What is the most likely cause if the data volume is consistent?",
            "options": [
                "The state store is being kept in memory and has grown too large for the executor's heap.",
                "The shuffle partitions are set too high, causing small file overhead.",
                "The watermark is being applied after the `groupBy()` instead of before.",
                "The output mode is set to 'Complete' which causes the entire state to be written every time."
            ],
            "answer": 0,
            "explanation": "By default, Spark uses an in-memory HDFS state store. For large states, switching to the RocksDB state store (which stores state on disk) is necessary to avoid OOMs."
        },
        {
            "q": "In Unity Catalog, you want to ensure that any table created in the `prod` catalog automatically inherits the same set of permissions granted at the catalog level. Which principle describes this behavior?",
            "options": [
                "Privilege Inheritance",
                "Dynamic Granting",
                "Cascade Authorization",
                "Implicit Ownership"
            ],
            "answer": 0,
            "explanation": "In Unity Catalog, privileges are inherited downward from the Catalog to the Schema, and from the Schema to the Table/View."
        },
        {
            "q": "Which SQL clause allows you to filter the results of a window function (like `rank()` or `row_number()`) without using a subquery or a Common Table Expression (CTE)?",
            "options": [
                "QUALIFY",
                "HAVING",
                "FILTER",
                "WHERE"
            ],
            "answer": 0,
            "explanation": "The `QUALIFY` clause filters the results of window functions in the same way that `HAVING` filters the results of aggregate functions."
        },
        {
            "q": "You observe in the Spark UI that a join is taking a long time, and the 'Summary Metrics' for the stage show a large difference between 'Median' and 'Max' task duration. Additionally, some tasks show 'Spill (Disk)'. What is the most effective way to address this?",
            "options": [
                "Enable Adaptive Query Execution (AQE) and its skew join optimization.",
                "Increase the number of cores on the driver node.",
                "Set `spark.sql.shuffle.partitions` to a much lower number.",
                "Use the `coalesce()` method on the DataFrames before the join."
            ],
            "answer": 0,
            "explanation": "AQE skew join optimization detects skewed partitions and splits them into smaller pieces, balancing the work and eliminating disk spilling for those tasks."
        },
        {
            "q": "A Delta table has a property `delta.minReaderVersion` set to 2. A user attempts to read the table from an older version of Spark that only supports Delta protocol version 1. What will happen?",
            "options": [
                "The read will fail with an error stating the reader version is unsupported.",
                "The read will succeed but will skip any columns created using new features.",
                "The read will succeed but will be significantly slower due to emulation mode.",
                "The Delta table will automatically downgrade its protocol version to accommodate the user."
            ],
            "answer": 0,
            "explanation": "Delta protocol versions ensure that clients don't read data containing features they don't understand, preventing silent data corruption or errors."
        },
        {
            "q": "In a PySpark DataFrame, you have a column `raw_json` of type STRING. You want to extract a specific field `nested.id` and cast it to an INTEGER. Which approach is most performant and syntactically correct?",
            "options": [
                "from_json(col(\"raw_json\"), schema).getField(\"nested\").getField(\"id\").cast(\"int\")",
                "raw_json.map(lambda x: json.loads(x)['nested']['id'])",
                "get_json_object(col(\"raw_json\"), \"$.nested.id\").cast(\"int\")",
                "regexp_extract(col(\"raw_json\"), \"'id': (\\\\d+)\", 1).cast(\"int\")"
            ],
            "answer": 0,
            "explanation": "Using `from_json` with a pre-defined schema allows Spark to efficiently parse only the needed fields and integrate them into the DataFrame's native execution plan."
        },
        {
            "q": "When creating a **Managed Volume** in Unity Catalog, where is the physical data stored?",
            "options": [
                "In the default storage location associated with the Schema or Catalog.",
                "In the Databricks internal DBFS (Databricks File System) root.",
                "On the local SSDs of the Spark worker nodes.",
                "In a specific S3 path that must be provided during the `CREATE VOLUME` command."
            ],
            "answer": 0,
            "explanation": "Managed Volumes, like Managed Tables, use the storage path defined at the Schema or Catalog level in Unity Catalog."
        },
        {
            "q": "A Data Engineer is using `dbutils.jobs.taskValues.set()` in a task named 'Ingest'. They want to use this value in a 'Filter' task that follows. What is the correct way to reference this value in a SQL-based Filter task?",
            "options": [
                "{{tasks.Ingest.values.my_key}}",
                "dbutils.jobs.taskValues.get('Ingest', 'my_key')",
                "$Ingest.my_key",
                "SELECT * FROM task_values WHERE task = 'Ingest'"
            ],
            "answer": 0,
            "explanation": "Databricks Workflows use a double-curly-brace syntax to inject task values dynamically into task parameters or SQL queries."
        },
        {
            "q": "You are building a DLT pipeline where a Silver table depends on two different Bronze tables. You want to ensure the Silver table only updates when *both* Bronze tables have new data. Is this possible in DLT?",
            "options": [
                "No, DLT tables update as soon as any of their upstream dependencies have new data available.",
                "Yes, by setting the `pipelines.sync.wait_for_all` configuration to `true`.",
                "Yes, by using a `@dlt.expect_all` rule that checks the `_ingested_timestamp` of both sources.",
                "Yes, but only if both Bronze tables are defined as `STREAMING LIVE` tables."
            ],
            "answer": 0,
            "explanation": "DLT is designed for continuous or triggered data flow; it does not natively support 'barrier' logic where it waits for multiple sources to be 'ready' simultaneously before processing."
        },
        {
            "q": "What is the primary benefit of using a **Shallow Clone** over a **Deep Clone** for a multi-terabyte table being used for testing?",
            "options": [
                "It is nearly instantaneous and consumes virtually no additional storage.",
                "It creates a physically separate copy of the data to prevent accidental deletions in production.",
                "It allows the clone to be read by external tools that don't support Delta Lake.",
                "It automatically synchronizes changes from the source table to the clone."
            ],
            "answer": 0,
            "explanation": "A shallow clone only copies the transaction log (metadata), not the data files, making it extremely fast regardless of table size."
        },
        {
            "q": "An analyst is querying an Information Schema view to find all tables they have permission to read. Which view should they query?",
            "options": [
                "information_schema.table_privileges",
                "information_schema.tables",
                "system.access.audit_log",
                "information_schema.catalog_privileges"
            ],
            "answer": 0,
            "explanation": "The `table_privileges` view in the `information_schema` provides a comprehensive list of all privileges granted on tables and views."
        },
        {
            "q": "In Spark Structured Streaming, which output mode is the only one supported when the query does NOT contain any aggregations?",
            "options": [
                "Append",
                "Complete",
                "Update",
                "Overwrite"
            ],
            "answer": 0,
            "explanation": "Without an aggregation, there is no state to 'update' or 'complete', so only new rows can be appended to the sink."
        },
        {
            "q": "You are creating a table with a column `id` that should automatically increment for every new row. However, you want to allow users to manually provide their own `id` if necessary. Which syntax should you use?",
            "options": [
                "id BIGINT GENERATED BY DEFAULT AS IDENTITY",
                "id BIGINT GENERATED ALWAYS AS IDENTITY",
                "id BIGINT AUTO_INCREMENT",
                "id BIGINT DEFAULT (next_value())"
            ],
            "answer": 0,
            "explanation": "`BY DEFAULT` allows the system to generate a value while still permitting manual overrides. `ALWAYS` would block manual inserts."
        },
        {
            "q": "When configuring a Databricks Job with multiple tasks, you want a specific task to run even if the previous task failed, so that you can perform cleanup. Which 'Run if' condition should you select?",
            "options": [
                "At least one dependency failed",
                "All dependencies succeeded",
                "Dependencies completed",
                "Always"
            ],
            "answer": 0,
            "explanation": "This ensures the cleanup task runs only when things go wrong, preventing unnecessary execution during successful runs."
        },
        {
            "q": "What is the result of running `VACUUM` on a table where the Change Data Feed (CDF) is enabled?",
            "options": [
                "It removes old data files but keeps the CDF log files according to the `delta.columnMapping.maxId` property.",
                "It removes old data files, and any CDF data referencing those deleted files will no longer be queryable.",
                "It is not possible to run `VACUUM` on a table with CDF enabled.",
                "It only removes files that are at least 30 days old, regardless of the `RETAIN` parameter, to protect the CDF."
            ],
            "answer": 1,
            "explanation": "Because CDF relies on the existence of the version-specific files, vacuuming the data files will break the ability to read changes for those specific versions."
        },
        {
            "q": "In PySpark, what is the key difference between `repartition()` and `coalesce()` when reducing the number of partitions?",
            "options": [
                "`repartition()` performs a full shuffle to balance data, while `coalesce()` avoids a shuffle by merging adjacent partitions.",
                "`repartition()` can only increase partitions, while `coalesce()` can only decrease them.",
                "`coalesce()` is faster because it runs on the driver, while `repartition()` runs on executors.",
                "`repartition()` is only for Delta tables, while `coalesce()` is for all DataFrames."
            ],
            "answer": 0,
            "explanation": "`coalesce` is more efficient for reducing partitions because it minimizes data movement, whereas `repartition` is better for ensuring even data distribution at the cost of a shuffle."
        }
    ]
}