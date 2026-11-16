import { sqliteTable, text, integer, index } from 'drizzle-orm/sqlite-core';

export const enquiries = sqliteTable('enquiries', {
  id: text('id').primaryKey(),
  createdAt: text('created_at').notNull(),
  name: text('name').notNull(),
  email: text('email').notNull(),
  organization: text('organization').notNull().default(''),
  phone: text('phone').notNull().default(''),
  preferredTime: text('preferred_time').notNull().default(''),
  topic: text('topic').notNull(),
  replyBy: text('reply_by').notNull(),
  message: text('message').notNull(),
  portfolioUrl: text('portfolio_url').notNull().default(''),
  language: text('language').notNull(),
  marketingOptIn: integer('marketing_opt_in').notNull().default(0),
  marketingConsentText: text('marketing_consent_text').notNull(),
  marketingConsentVersion: text('marketing_consent_version').notNull(),
  marketingConsentedAt: text('marketing_consented_at'),
  privacyNoticeVersion: text('privacy_notice_version').notNull(),
  rateKey: text('rate_key').notNull(),
  reviewedAt: text('reviewed_at'),
}, (table) => [
  index('enquiries_created_idx').on(table.createdAt),
  index('enquiries_email_idx').on(table.email, table.createdAt),
  index('enquiries_rate_idx').on(table.rateKey, table.createdAt),
]);
