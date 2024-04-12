# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) (with possible titles of 'added', 'changed', 'deprecated', 'removed', 'fixed', or 'security'),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This should align with releases on [GitHub](https://github.com/kailo-beewell/synthetic_symbol_school_dashboard_stable_release/releases) (which is like a non-portable changelog only displayed to users within GitHub)

Writing of this changelog is supported by comparison of main and forked repositories on GitHub, and from [changelog of the kailo_beewell_dashboard package](https://github.com/kailo-beewell/kailo_beewell_dashboard_package/blob/main/CHANGELOG.md).

## 0.1.1

**Release date:** 12th April 2024

**Contributors:** Amy Heather

Modifications to work with kailo_beewell_dashboard==0.3.2

### Changed

* Using new functions (e.g. get_image_path, create_about_page, aggregation, demographic labels)

### Fixed

* Corrected issue where page_footer was outside the boundary of check_password()

### Removed

* CSS style sheets (now within package)

## 0.1.0

**Release date:** 18th March 2024

**Contributors:** Amy Heather

First stable forked release of the synthetic symbol survey dashboard, using kailo_beewell_dashboard==0.2.0.

### Added

* Home page (including option to download static PDF report with results)
* About page
* Explore results page (for all pupils, by year group, by gender and by FSM)
* Who took part page
