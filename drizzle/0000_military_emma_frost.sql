CREATE TABLE `enquiries` (
	`id` text PRIMARY KEY NOT NULL,
	`created_at` text NOT NULL,
	`name` text NOT NULL,
	`email` text NOT NULL,
	`organization` text DEFAULT '' NOT NULL,
	`phone` text DEFAULT '' NOT NULL,
	`preferred_time` text DEFAULT '' NOT NULL,
	`topic` text NOT NULL,
	`reply_by` text NOT NULL,
	`message` text NOT NULL,
	`portfolio_url` text DEFAULT '' NOT NULL,
	`language` text NOT NULL,
	`marketing_opt_in` integer DEFAULT 0 NOT NULL,
	`marketing_consent_text` text NOT NULL,
	`marketing_consent_version` text NOT NULL,
	`marketing_consented_at` text,
	`privacy_notice_version` text NOT NULL,
	`rate_key` text NOT NULL,
	`reviewed_at` text
);
--> statement-breakpoint
CREATE INDEX `enquiries_created_idx` ON `enquiries` (`created_at`);--> statement-breakpoint
CREATE INDEX `enquiries_email_idx` ON `enquiries` (`email`,`created_at`);--> statement-breakpoint
CREATE INDEX `enquiries_rate_idx` ON `enquiries` (`rate_key`,`created_at`);