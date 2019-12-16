#Column Names for the different extracts that are downloadable from CALPADS. These are subject to change over time.
EXTRACT_COLUMNS = {
        'SENR': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'SchoolOfAttendanceNPS', 'AcademicYearID',
            'SSID', 'LocalStudentID', 'StudentLegalFirstName', 'StudentLegalMiddleName', 'StudentLegalLastName', 'StudentLegalNameSuffix', 'StudentAliasFirstName',
            'StudentAliasMiddleName', 'StudentAliasLastName', 'StudentBirthDate', 'StudentGenderCode', 'StudentBirthCity', 'StudentBirthStateProvinceCode',
            'StudentBirthCountryCode', 'EnrollmentSchoolStartDate', 'EnrollmentStatusCode', 'GradeLevelCode', 'EnrollmentSchoolExitDate', 'StudentExitReasonCode',
            'StudentSchoolCompletionStatus', 'ExpectedReceiverSchoolofAttendance', 'StudentMetAllUCCSURequirementsIndicator', 'StudentSchoolTransferCode',
            'DistrictofGeographicResidence', 'StudentGoldenStateSealMeritDiplomaIndicator', 'StudentSealofBiliteracyIndicator', 'PostsecondaryTransitionStatusIndicator',
            'WorkforceReadinessStrategicSkillsCertificateProgramCompletionIndicator', 'FoodHandlerCertificationProgramCompletionIndicator',
            'PreApprenticeshipCertificationProgramCompletionIndicator', 'PreApprenticeshipProgramNonCertifiedCompletionIndicator', 'StateFederalJobProgramCompletionIndicator',
            'UploadDate', 'LastDateUpdated'],
        'SINF': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'EffectiveStartDate', 'EffectiveEndDate', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID',
            'LocalStudentID', 'StudentLegalFirstName', 'StudentLegalMiddleName', 'StudentLegalLastName', 'StudentLegalNameSuffix', 'StudentAliasFirstName', 'StudentAliasMiddleName',
            'StudentAliasLastName', 'StudentBirthDate', 'StudentGenderCode', 'StudentBirthCity', 'StudentBirthStateProvinceCode', 'StudentBirthCountryCode',
            'StudentHispanicEthnicityIndicator', 'StudentEthnicityMissingIndicator', 'StudentRace1Code', 'StudentRace2Code', 'StudentRace3Code', 'StudentRace4Code', 'StudentRace5Code',
            'StudentRaceMissingIndicator', 'AddressLine1', 'AddressLine2', 'AddressCityName', 'AddressStateProvinceCode', 'AddressZipCode', 'StudentInitialUSSchoolEnrollmentDateK-12',
            'EnrolledinUSSchoollessthanThreeCumulativeYearsIndicator', 'ParentGuardianHighestEducationLevelCode', 'Guardian1FirstName', 'Guardian1LastName', 'Guardian2FirstName',
            'Guardian2LastName', 'UploadDate', 'LastDateUpdated'],
        'SELA': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID',
            'StudentLegalFirstName', 'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'LocalStudentID', 'EnglishAcquisitionStatusCode',
            'EnglishAcquisitionStatusStartDate', 'PrimaryLanguageCode', 'UploadDate', 'LastDateUpdated'],
        'SPRG': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
            'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'EducationProgramCode', 'EducationProgramMembershipCode', 'EducationProgramMembershipStartDate',
            'EducationProgramMembershipEndDate', 'EducationServiceAcademicYear', 'EducationServiceCode', 'CaliforniaPartnershipAcademyID', 'MigrantStudentID',
            'PrimaryDisabilityCode', 'DistrictofSpecialEducationAccountability', 'HomelessDwellingTypeCode', 'UnaccompaniedYouthIndicator', 'RunawayYouthIndicator', 'Filler',
            'UploadDate', 'LastDateUpdated'],
        'CENR': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'SchoolOfAttendanceNPS', 'AcademicYearID',
            'SSID', 'LocalStudentID', 'StudentLegalFirstName', 'StudentLegalMiddleName', 'StudentLegalLastName', 'StudentLegalNameSuffix', 'StudentAliasFirstName',
            'StudentAliasMiddleName', 'StudentAliasLastName', 'StudentBirthDate', 'StudentGenderCode', 'StudentBirthCity', 'StudentBirthStateProvinceCode',
            'StudentBirthCountryCode', 'EnrollmentSchoolStartDate', 'EnrollmentStatusCode', 'GradeLevelCode', 'EnrollmentSchoolExitDate', 'StudentExitReasonCode',
            'StudentSchoolCompletionStatus', 'ExpectedReceiverSchoolofAttendance', 'StudentMetAllUCCSURequirementsIndicator', 'StudentSchoolTransferCode',
            'DistrictofGeographicResidence', 'StudentGoldenStateSealMeritDiplomaIndicator', 'StudentSealofBiliteracyIndicator', 'UploadDate', 'LastDateUpdated'],
        'DIRECTCERTIFICATION': ["Academic Year", "Reporting LEA", "School of Attendance", "Local Student ID", "SSID",
                        "Student Legal First Name", "Student Legal Middle Name", "Student Legal Last Name", "Certification Date",
                        "Certification Status"],
        'SSID': ['ReportingLEA', 'SchoolOfAttendance', 'SSID', 'LocalStudentID', 'StudentLegalLastName', 'StudentLegalFirstName', 'GenderCode',
            'StudentBirthDate', 'EnrollmentStartDate', 'GradeLevelCode', 'EnglishLanguageAcquisitionStatusCode', 'EnglishLanguageAcquisitionStatusStartDate', 'PrimaryLanguage',
            'DateSSIDCreated'],
        'SDEM': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'EffectiveStartDate', 'EffectiveEndDate', 'ReportingLEA', 'AcademicYearID', 'SEID', 'LocalStaffID',
            'StaffLegalFirstName', 'StaffLegalMiddleName', 'StaffLegalLastName', 'StaffAliasFirstName', 'StaffAliasMiddleName', 'StaffAliasLastName', 'StaffBirthDate',
            'StaffGenderCode', 'StaffHispanicEthnicityIndicator', 'StaffEthnicityMissingIndicator', 'StaffRace1Code', 'StaffRace2Code', 'StaffRace3Code', 'StaffRace4Code',
            'StaffRace5Code', 'StaffRaceMissingIndicator', 'StaffHighestDegreeCode', 'StaffEmploymentStatusCode', 'StaffEmploymentStartDate', 'StaffEmploymentEndDate',
            'StaffServiceYearsLEA', 'StaffServiceYearsTotal', 'UploadDate', 'LastDateUpdated'],
        'SASS': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolofAssignment', 'AcademicYearID', 'SEID', 'LocalStaffID', 'StaffLegalFirstName',
            'StaffLegalLastName', 'StaffBirthDate', 'StaffGenderCode', 'StaffJobClassificationCode', 'StaffJobClassificationFTEPercentage', 'NonClassroomBasedJobAssignmentCode1',
            'NonClassroomBasedJobAssignmentCode2', 'NonClassroomBasedJobAssignmentCode3', 'NonClassroomBasedJobAssignmentCode4', 'NonClassroomBasedJobAssignmentCode5',
            'NonClassroomBasedJobAssignmentCode6', 'NonClassroomBasedJobAssignmentCode7', 'UploadDate', 'LastDateUpdated'],
        'SDIS': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
             'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'DisciplinaryIncidentIDLocal', 'DisciplinaryIncidentOccurrenceDate', 'StudentOffenseCode',
             'IncidentMostSevereOffenseCode', 'WeaponCategoryCode', 'IncidentDisciplinaryActionTakenCode', 'DisciplinaryActionAuthorityCode', 'IncidentDisciplinaryActionDurationDays',
             'StudentInstructionalSupportIndicator', 'DisciplinaryActionModificationCategoryCode', 'RemovaltoInterimAlternativeSettingReasonCode', 'UploadDate', 'LastDateUpdated'],
        'STAS': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
            'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'StudentAbsenceSummaryDataCollectionExemptionIndicator', 'HourlyAttendanceSchoolTypeIndicator',
            'ExpectedAttendanceDays', 'DaysAttended', 'DaysAbsentOut-of-SchoolSuspension', 'DaysinAttendanceIn-SchoolSuspension', 'DaysAbsentExcusedNon-Suspension',
            'DaysAbsentUnexcusedNon-Suspension', 'IncompleteIndependentStudyDays', 'UploadDate', 'LastDateUpdated'],
        'CRSE': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolofCourseDelivery', 'AcademicYearID', 'CRS-StateCourseCode', 'CRS-LocalCourseID',
            'CRS-CourseName', 'CRS-CourseContentCode', 'Filler', 'CRS-CTETechnicalPreparationCourseIndicator', 'CRS-UCCSUApprovedIndicator', 'CourseSectionID', 'AcademicTermCode',
            'SEID', 'LocalStaffID', 'ClassID', 'CourseSectionInstructionalLevelCode', 'EducationServiceCode', 'LanguageofInstructionCode', 'InstructionalStrategyCode',
            'IndependentStudyIndicator', 'DistanceLearningIndicator', 'MultipleTeacherCode', 'EducationProgramFundingSourceCode', 'CTECourseSectionProviderCode', 
            'UplodadDate', 'LastDateUpdated'],
        'CRSC': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolofCourseDelivery', 'AcademicYearID', 'CRS-StateCourseCode', 'CRS-LocalCourseID',
            'CRS-CourseName', 'CRS-CourseContentCode', 'Filler', 'CRS-CTETechnicalPreparationCourseIndicator', 'CRS-UCCSUApprovedIndicator', 'CourseSectionID', 'AcademicTermCode',
            'SEID', 'LocalStaffID', 'ClassID', 'CourseSectionInstructionalLevelCode', 'EducationServiceCode', 'LanguageofInstructionCode', 'InstructionalStrategyCode',
            'IndependentStudyIndicator', 'DistanceLearningIndicator', 'MultipleTeacherCode', 'EducationProgramFundingSourceCode', 'CTECourseSectionProviderCode', 
            'UplodadDate', 'LastDateUpdated'],
        'SCSE': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
            'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'LocalCourseID', 'CourseSectionID', 'AcademicTermCode', 'StudentCreditsAttempted',
            'StudentCreditsEarned', 'StudentCourseFinalGrade', 'UC_CSUAdmissionRequirementCode', 'MarkingPeriodCode', 'UploadDate', 'LastDateUpdated'],
        'SCSC': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
            'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'LocalCourseID', 'CourseSectionID', 'AcademicTermCode', 'StudentCreditsAttempted',
            'StudentCreditsEarned', 'StudentCourseFinalGrade', 'UC_CSUAdmissionRequirementCode', 'MarkingPeriodCode', 'UploadDate', 'LastDateUpdated'],
        'SCTE': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'AcademicYearID', 'SSID', 'LocalStudentID', 'StudentLegalFirstName',
            'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'CTEPathwayCode', 'StudentCTEPathwayCompletionAcademicYearID', 'UploadDate', 'LastDateUpdated'],
        'SPED': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'SchoolOfAttendanceNPS', 'AcademicYearID', 'SSID', 'LocalStudentID',
                'LocalSpecialEducationStudentID', 'StudentLegalFirstName', 'StudentLegalLastName', 'StudentBirthDate', 'StudentGenderCode', 'ReportingSELPA',
                'DistrictOfSpecialEducationAccountability', 'SpecialEducationReferralDate', 'ReferringPartyCode', 'InitialEvaluationParentalConsentDate',
                'SpecialEducationMeetingTypeCode', 'SpecialEducationMeetingDate', 'StudentSpecialEducationMeetingOrAmendmentIdentifier', 'MeetingDelayCode', 'EducationPlanTypeCode',
                'EducationPlanAmendmentDate', 'PrimaryResidenceCode', 'SpecialEducationInitialEntryStartDate', 'Disability1Code', 'Disability2Code',
                'InfantRegionalCenterServicesEligibilityIndicator', 'SpecialEducationProgramSettingCode', 'PreschoolProgramSettingServiceLocationCode',
                'TenOrMoreWeeklyHoursInSettingIndicator', 'GeneralEducationParticipationPercentageRangeCode', 'SpecialEducationProgramTypeCode',
                'IEPIncludesPostsecondaryGoalsIndicator', 'PostsecondaryGoalsUpdatedAnnuallyIndicator', 'PostsecondaryGoalsAgeAppropriateTransitionAssessmentIndicator',
                'TransitionServicesInIEPIndicator', 'SupportiveServicesIndicator', 'TransitionServicesGoalsInIEPIndicator', 'StudentIEPParticipationIndicator',
                'AgencyRepresentativeIEPParticipationCode', 'SpecialTransportationIndicator', 'ParentalInvolvementFacilitationCode', 'SpecialEducationProgramExitDate',
                'WorkabilityIWorkBasedLearningProgramCompletionIndicator', 'DepartmentOfRehabilitationStudentServicesWorkBasedLearningProgramCompletionIndicator',
                'SpecialEducationProgramExitReasonCode', 'StudentHispanicEthnicityIndicator', 'StudentEthnicityMissingIndicator', 'StudentRace1Code', 'StudentRace2Code',
                'StudentRace3Code', 'StudentRace4Code', 'StudentRace5Code', 'StudentRaceMissingIndicator', 'UploadDate', 'LastDateUpdated'],
        'SSRV': ['RecordTypeCode', 'TransactionTypeCode', 'LocalRecordID', 'ReportingLEA', 'SchoolOfAttendance', 'SchoolOfAttendanceNPS',
                'NonpublicAgencyIdentifierNPA', 'AcademicYearID', 'SSID', 'ReportingSELPA', 'DistrictOfSpecialEducationAccountability',
                'StudentSpecialEducationMeetingOrAmendmentIdentifier', 'SpecialEducationServiceCode', 'SpecialEducationServiceProviderCode',
                'SpecialEducationServiceLocationCode', 'ServiceFrequencyCode', 'ServiceDuration', 'LocalSpecialEducationStudentID', 'UploadDate', 'LastDateUpdated']

}