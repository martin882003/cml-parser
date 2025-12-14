# Generated from CML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMLParser import CMLParser
else:
    from CMLParser import CMLParser

# This class defines a complete listener for a parse tree produced by CMLParser.
class CMLListener(ParseTreeListener):

    # Enter a parse tree produced by CMLParser#definitions.
    def enterDefinitions(self, ctx:CMLParser.DefinitionsContext):
        pass

    # Exit a parse tree produced by CMLParser#definitions.
    def exitDefinitions(self, ctx:CMLParser.DefinitionsContext):
        pass


    # Enter a parse tree produced by CMLParser#imports.
    def enterImports(self, ctx:CMLParser.ImportsContext):
        pass

    # Exit a parse tree produced by CMLParser#imports.
    def exitImports(self, ctx:CMLParser.ImportsContext):
        pass


    # Enter a parse tree produced by CMLParser#topLevel.
    def enterTopLevel(self, ctx:CMLParser.TopLevelContext):
        pass

    # Exit a parse tree produced by CMLParser#topLevel.
    def exitTopLevel(self, ctx:CMLParser.TopLevelContext):
        pass


    # Enter a parse tree produced by CMLParser#contextMap.
    def enterContextMap(self, ctx:CMLParser.ContextMapContext):
        pass

    # Exit a parse tree produced by CMLParser#contextMap.
    def exitContextMap(self, ctx:CMLParser.ContextMapContext):
        pass


    # Enter a parse tree produced by CMLParser#contextMapSetting.
    def enterContextMapSetting(self, ctx:CMLParser.ContextMapSettingContext):
        pass

    # Exit a parse tree produced by CMLParser#contextMapSetting.
    def exitContextMapSetting(self, ctx:CMLParser.ContextMapSettingContext):
        pass


    # Enter a parse tree produced by CMLParser#contextMapType.
    def enterContextMapType(self, ctx:CMLParser.ContextMapTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#contextMapType.
    def exitContextMapType(self, ctx:CMLParser.ContextMapTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#contextMapState.
    def enterContextMapState(self, ctx:CMLParser.ContextMapStateContext):
        pass

    # Exit a parse tree produced by CMLParser#contextMapState.
    def exitContextMapState(self, ctx:CMLParser.ContextMapStateContext):
        pass


    # Enter a parse tree produced by CMLParser#relationship.
    def enterRelationship(self, ctx:CMLParser.RelationshipContext):
        pass

    # Exit a parse tree produced by CMLParser#relationship.
    def exitRelationship(self, ctx:CMLParser.RelationshipContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipConnection.
    def enterRelationshipConnection(self, ctx:CMLParser.RelationshipConnectionContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipConnection.
    def exitRelationshipConnection(self, ctx:CMLParser.RelationshipConnectionContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipEndpoint.
    def enterRelationshipEndpoint(self, ctx:CMLParser.RelationshipEndpointContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipEndpoint.
    def exitRelationshipEndpoint(self, ctx:CMLParser.RelationshipEndpointContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipEndpointRight.
    def enterRelationshipEndpointRight(self, ctx:CMLParser.RelationshipEndpointRightContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipEndpointRight.
    def exitRelationshipEndpointRight(self, ctx:CMLParser.RelationshipEndpointRightContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipKeyword.
    def enterRelationshipKeyword(self, ctx:CMLParser.RelationshipKeywordContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipKeyword.
    def exitRelationshipKeyword(self, ctx:CMLParser.RelationshipKeywordContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipRoles.
    def enterRelationshipRoles(self, ctx:CMLParser.RelationshipRolesContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipRoles.
    def exitRelationshipRoles(self, ctx:CMLParser.RelationshipRolesContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipRole.
    def enterRelationshipRole(self, ctx:CMLParser.RelationshipRoleContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipRole.
    def exitRelationshipRole(self, ctx:CMLParser.RelationshipRoleContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipArrow.
    def enterRelationshipArrow(self, ctx:CMLParser.RelationshipArrowContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipArrow.
    def exitRelationshipArrow(self, ctx:CMLParser.RelationshipArrowContext):
        pass


    # Enter a parse tree produced by CMLParser#relationshipAttribute.
    def enterRelationshipAttribute(self, ctx:CMLParser.RelationshipAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#relationshipAttribute.
    def exitRelationshipAttribute(self, ctx:CMLParser.RelationshipAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#downstreamRights.
    def enterDownstreamRights(self, ctx:CMLParser.DownstreamRightsContext):
        pass

    # Exit a parse tree produced by CMLParser#downstreamRights.
    def exitDownstreamRights(self, ctx:CMLParser.DownstreamRightsContext):
        pass


    # Enter a parse tree produced by CMLParser#boundedContext.
    def enterBoundedContext(self, ctx:CMLParser.BoundedContextContext):
        pass

    # Exit a parse tree produced by CMLParser#boundedContext.
    def exitBoundedContext(self, ctx:CMLParser.BoundedContextContext):
        pass


    # Enter a parse tree produced by CMLParser#boundedContextLinkClause.
    def enterBoundedContextLinkClause(self, ctx:CMLParser.BoundedContextLinkClauseContext):
        pass

    # Exit a parse tree produced by CMLParser#boundedContextLinkClause.
    def exitBoundedContextLinkClause(self, ctx:CMLParser.BoundedContextLinkClauseContext):
        pass


    # Enter a parse tree produced by CMLParser#boundedContextAttribute.
    def enterBoundedContextAttribute(self, ctx:CMLParser.BoundedContextAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#boundedContextAttribute.
    def exitBoundedContextAttribute(self, ctx:CMLParser.BoundedContextAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#boundedContextType.
    def enterBoundedContextType(self, ctx:CMLParser.BoundedContextTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#boundedContextType.
    def exitBoundedContextType(self, ctx:CMLParser.BoundedContextTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#knowledgeLevel.
    def enterKnowledgeLevel(self, ctx:CMLParser.KnowledgeLevelContext):
        pass

    # Exit a parse tree produced by CMLParser#knowledgeLevel.
    def exitKnowledgeLevel(self, ctx:CMLParser.KnowledgeLevelContext):
        pass


    # Enter a parse tree produced by CMLParser#evolutionType.
    def enterEvolutionType(self, ctx:CMLParser.EvolutionTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#evolutionType.
    def exitEvolutionType(self, ctx:CMLParser.EvolutionTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#domain.
    def enterDomain(self, ctx:CMLParser.DomainContext):
        pass

    # Exit a parse tree produced by CMLParser#domain.
    def exitDomain(self, ctx:CMLParser.DomainContext):
        pass


    # Enter a parse tree produced by CMLParser#subdomain.
    def enterSubdomain(self, ctx:CMLParser.SubdomainContext):
        pass

    # Exit a parse tree produced by CMLParser#subdomain.
    def exitSubdomain(self, ctx:CMLParser.SubdomainContext):
        pass


    # Enter a parse tree produced by CMLParser#subdomainType.
    def enterSubdomainType(self, ctx:CMLParser.SubdomainTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#subdomainType.
    def exitSubdomainType(self, ctx:CMLParser.SubdomainTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#module.
    def enterModule(self, ctx:CMLParser.ModuleContext):
        pass

    # Exit a parse tree produced by CMLParser#module.
    def exitModule(self, ctx:CMLParser.ModuleContext):
        pass


    # Enter a parse tree produced by CMLParser#tacticDDDApplication.
    def enterTacticDDDApplication(self, ctx:CMLParser.TacticDDDApplicationContext):
        pass

    # Exit a parse tree produced by CMLParser#tacticDDDApplication.
    def exitTacticDDDApplication(self, ctx:CMLParser.TacticDDDApplicationContext):
        pass


    # Enter a parse tree produced by CMLParser#tacticDDDElement.
    def enterTacticDDDElement(self, ctx:CMLParser.TacticDDDElementContext):
        pass

    # Exit a parse tree produced by CMLParser#tacticDDDElement.
    def exitTacticDDDElement(self, ctx:CMLParser.TacticDDDElementContext):
        pass


    # Enter a parse tree produced by CMLParser#aggregate.
    def enterAggregate(self, ctx:CMLParser.AggregateContext):
        pass

    # Exit a parse tree produced by CMLParser#aggregate.
    def exitAggregate(self, ctx:CMLParser.AggregateContext):
        pass


    # Enter a parse tree produced by CMLParser#domainObject.
    def enterDomainObject(self, ctx:CMLParser.DomainObjectContext):
        pass

    # Exit a parse tree produced by CMLParser#domainObject.
    def exitDomainObject(self, ctx:CMLParser.DomainObjectContext):
        pass


    # Enter a parse tree produced by CMLParser#simpleDomainObjectOrEnum.
    def enterSimpleDomainObjectOrEnum(self, ctx:CMLParser.SimpleDomainObjectOrEnumContext):
        pass

    # Exit a parse tree produced by CMLParser#simpleDomainObjectOrEnum.
    def exitSimpleDomainObjectOrEnum(self, ctx:CMLParser.SimpleDomainObjectOrEnumContext):
        pass


    # Enter a parse tree produced by CMLParser#simpleDomainObject.
    def enterSimpleDomainObject(self, ctx:CMLParser.SimpleDomainObjectContext):
        pass

    # Exit a parse tree produced by CMLParser#simpleDomainObject.
    def exitSimpleDomainObject(self, ctx:CMLParser.SimpleDomainObjectContext):
        pass


    # Enter a parse tree produced by CMLParser#entity.
    def enterEntity(self, ctx:CMLParser.EntityContext):
        pass

    # Exit a parse tree produced by CMLParser#entity.
    def exitEntity(self, ctx:CMLParser.EntityContext):
        pass


    # Enter a parse tree produced by CMLParser#entityBody.
    def enterEntityBody(self, ctx:CMLParser.EntityBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#entityBody.
    def exitEntityBody(self, ctx:CMLParser.EntityBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#entityFlag.
    def enterEntityFlag(self, ctx:CMLParser.EntityFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#entityFlag.
    def exitEntityFlag(self, ctx:CMLParser.EntityFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#valueObject.
    def enterValueObject(self, ctx:CMLParser.ValueObjectContext):
        pass

    # Exit a parse tree produced by CMLParser#valueObject.
    def exitValueObject(self, ctx:CMLParser.ValueObjectContext):
        pass


    # Enter a parse tree produced by CMLParser#valueObjectBody.
    def enterValueObjectBody(self, ctx:CMLParser.ValueObjectBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#valueObjectBody.
    def exitValueObjectBody(self, ctx:CMLParser.ValueObjectBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#valueObjectFlag.
    def enterValueObjectFlag(self, ctx:CMLParser.ValueObjectFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#valueObjectFlag.
    def exitValueObjectFlag(self, ctx:CMLParser.ValueObjectFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#domainEvent.
    def enterDomainEvent(self, ctx:CMLParser.DomainEventContext):
        pass

    # Exit a parse tree produced by CMLParser#domainEvent.
    def exitDomainEvent(self, ctx:CMLParser.DomainEventContext):
        pass


    # Enter a parse tree produced by CMLParser#domainEventBody.
    def enterDomainEventBody(self, ctx:CMLParser.DomainEventBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#domainEventBody.
    def exitDomainEventBody(self, ctx:CMLParser.DomainEventBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#domainEventFlag.
    def enterDomainEventFlag(self, ctx:CMLParser.DomainEventFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#domainEventFlag.
    def exitDomainEventFlag(self, ctx:CMLParser.DomainEventFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#commandEvent.
    def enterCommandEvent(self, ctx:CMLParser.CommandEventContext):
        pass

    # Exit a parse tree produced by CMLParser#commandEvent.
    def exitCommandEvent(self, ctx:CMLParser.CommandEventContext):
        pass


    # Enter a parse tree produced by CMLParser#commandEventBody.
    def enterCommandEventBody(self, ctx:CMLParser.CommandEventBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#commandEventBody.
    def exitCommandEventBody(self, ctx:CMLParser.CommandEventBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#commandEventFlag.
    def enterCommandEventFlag(self, ctx:CMLParser.CommandEventFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#commandEventFlag.
    def exitCommandEventFlag(self, ctx:CMLParser.CommandEventFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#trait.
    def enterTrait(self, ctx:CMLParser.TraitContext):
        pass

    # Exit a parse tree produced by CMLParser#trait.
    def exitTrait(self, ctx:CMLParser.TraitContext):
        pass


    # Enter a parse tree produced by CMLParser#traitBody.
    def enterTraitBody(self, ctx:CMLParser.TraitBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#traitBody.
    def exitTraitBody(self, ctx:CMLParser.TraitBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#traitFlag.
    def enterTraitFlag(self, ctx:CMLParser.TraitFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#traitFlag.
    def exitTraitFlag(self, ctx:CMLParser.TraitFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#traitRef.
    def enterTraitRef(self, ctx:CMLParser.TraitRefContext):
        pass

    # Exit a parse tree produced by CMLParser#traitRef.
    def exitTraitRef(self, ctx:CMLParser.TraitRefContext):
        pass


    # Enter a parse tree produced by CMLParser#dataTransferObject.
    def enterDataTransferObject(self, ctx:CMLParser.DataTransferObjectContext):
        pass

    # Exit a parse tree produced by CMLParser#dataTransferObject.
    def exitDataTransferObject(self, ctx:CMLParser.DataTransferObjectContext):
        pass


    # Enter a parse tree produced by CMLParser#dtoBody.
    def enterDtoBody(self, ctx:CMLParser.DtoBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#dtoBody.
    def exitDtoBody(self, ctx:CMLParser.DtoBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#dtoFlag.
    def enterDtoFlag(self, ctx:CMLParser.DtoFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#dtoFlag.
    def exitDtoFlag(self, ctx:CMLParser.DtoFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#dtoModifier.
    def enterDtoModifier(self, ctx:CMLParser.DtoModifierContext):
        pass

    # Exit a parse tree produced by CMLParser#dtoModifier.
    def exitDtoModifier(self, ctx:CMLParser.DtoModifierContext):
        pass


    # Enter a parse tree produced by CMLParser#enumDecl.
    def enterEnumDecl(self, ctx:CMLParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by CMLParser#enumDecl.
    def exitEnumDecl(self, ctx:CMLParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by CMLParser#enumOption.
    def enterEnumOption(self, ctx:CMLParser.EnumOptionContext):
        pass

    # Exit a parse tree produced by CMLParser#enumOption.
    def exitEnumOption(self, ctx:CMLParser.EnumOptionContext):
        pass


    # Enter a parse tree produced by CMLParser#enumAttribute.
    def enterEnumAttribute(self, ctx:CMLParser.EnumAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#enumAttribute.
    def exitEnumAttribute(self, ctx:CMLParser.EnumAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#enumValue.
    def enterEnumValue(self, ctx:CMLParser.EnumValueContext):
        pass

    # Exit a parse tree produced by CMLParser#enumValue.
    def exitEnumValue(self, ctx:CMLParser.EnumValueContext):
        pass


    # Enter a parse tree produced by CMLParser#enumParameter.
    def enterEnumParameter(self, ctx:CMLParser.EnumParameterContext):
        pass

    # Exit a parse tree produced by CMLParser#enumParameter.
    def exitEnumParameter(self, ctx:CMLParser.EnumParameterContext):
        pass


    # Enter a parse tree produced by CMLParser#basicType.
    def enterBasicType(self, ctx:CMLParser.BasicTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#basicType.
    def exitBasicType(self, ctx:CMLParser.BasicTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#basicTypeBody.
    def enterBasicTypeBody(self, ctx:CMLParser.BasicTypeBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#basicTypeBody.
    def exitBasicTypeBody(self, ctx:CMLParser.BasicTypeBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#basicTypeFlag.
    def enterBasicTypeFlag(self, ctx:CMLParser.BasicTypeFlagContext):
        pass

    # Exit a parse tree produced by CMLParser#basicTypeFlag.
    def exitBasicTypeFlag(self, ctx:CMLParser.BasicTypeFlagContext):
        pass


    # Enter a parse tree produced by CMLParser#feature.
    def enterFeature(self, ctx:CMLParser.FeatureContext):
        pass

    # Exit a parse tree produced by CMLParser#feature.
    def exitFeature(self, ctx:CMLParser.FeatureContext):
        pass


    # Enter a parse tree produced by CMLParser#association.
    def enterAssociation(self, ctx:CMLParser.AssociationContext):
        pass

    # Exit a parse tree produced by CMLParser#association.
    def exitAssociation(self, ctx:CMLParser.AssociationContext):
        pass


    # Enter a parse tree produced by CMLParser#attribute.
    def enterAttribute(self, ctx:CMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#attribute.
    def exitAttribute(self, ctx:CMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#attributeAssociationLabel.
    def enterAttributeAssociationLabel(self, ctx:CMLParser.AttributeAssociationLabelContext):
        pass

    # Exit a parse tree produced by CMLParser#attributeAssociationLabel.
    def exitAttributeAssociationLabel(self, ctx:CMLParser.AttributeAssociationLabelContext):
        pass


    # Enter a parse tree produced by CMLParser#attributeOption.
    def enterAttributeOption(self, ctx:CMLParser.AttributeOptionContext):
        pass

    # Exit a parse tree produced by CMLParser#attributeOption.
    def exitAttributeOption(self, ctx:CMLParser.AttributeOptionContext):
        pass


    # Enter a parse tree produced by CMLParser#notPrefix.
    def enterNotPrefix(self, ctx:CMLParser.NotPrefixContext):
        pass

    # Exit a parse tree produced by CMLParser#notPrefix.
    def exitNotPrefix(self, ctx:CMLParser.NotPrefixContext):
        pass


    # Enter a parse tree produced by CMLParser#attributeOptionKey.
    def enterAttributeOptionKey(self, ctx:CMLParser.AttributeOptionKeyContext):
        pass

    # Exit a parse tree produced by CMLParser#attributeOptionKey.
    def exitAttributeOptionKey(self, ctx:CMLParser.AttributeOptionKeyContext):
        pass


    # Enter a parse tree produced by CMLParser#oppositeHolder.
    def enterOppositeHolder(self, ctx:CMLParser.OppositeHolderContext):
        pass

    # Exit a parse tree produced by CMLParser#oppositeHolder.
    def exitOppositeHolder(self, ctx:CMLParser.OppositeHolderContext):
        pass


    # Enter a parse tree produced by CMLParser#operation.
    def enterOperation(self, ctx:CMLParser.OperationContext):
        pass

    # Exit a parse tree produced by CMLParser#operation.
    def exitOperation(self, ctx:CMLParser.OperationContext):
        pass


    # Enter a parse tree produced by CMLParser#callableOperationNoParens.
    def enterCallableOperationNoParens(self, ctx:CMLParser.CallableOperationNoParensContext):
        pass

    # Exit a parse tree produced by CMLParser#callableOperationNoParens.
    def exitCallableOperationNoParens(self, ctx:CMLParser.CallableOperationNoParensContext):
        pass


    # Enter a parse tree produced by CMLParser#operationWithParams.
    def enterOperationWithParams(self, ctx:CMLParser.OperationWithParamsContext):
        pass

    # Exit a parse tree produced by CMLParser#operationWithParams.
    def exitOperationWithParams(self, ctx:CMLParser.OperationWithParamsContext):
        pass


    # Enter a parse tree produced by CMLParser#operationNoParams.
    def enterOperationNoParams(self, ctx:CMLParser.OperationNoParamsContext):
        pass

    # Exit a parse tree produced by CMLParser#operationNoParams.
    def exitOperationNoParams(self, ctx:CMLParser.OperationNoParamsContext):
        pass


    # Enter a parse tree produced by CMLParser#operationPrefix.
    def enterOperationPrefix(self, ctx:CMLParser.OperationPrefixContext):
        pass

    # Exit a parse tree produced by CMLParser#operationPrefix.
    def exitOperationPrefix(self, ctx:CMLParser.OperationPrefixContext):
        pass


    # Enter a parse tree produced by CMLParser#operationHint.
    def enterOperationHint(self, ctx:CMLParser.OperationHintContext):
        pass

    # Exit a parse tree produced by CMLParser#operationHint.
    def exitOperationHint(self, ctx:CMLParser.OperationHintContext):
        pass


    # Enter a parse tree produced by CMLParser#operationHintType.
    def enterOperationHintType(self, ctx:CMLParser.OperationHintTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#operationHintType.
    def exitOperationHintType(self, ctx:CMLParser.OperationHintTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#operationClause.
    def enterOperationClause(self, ctx:CMLParser.OperationClauseContext):
        pass

    # Exit a parse tree produced by CMLParser#operationClause.
    def exitOperationClause(self, ctx:CMLParser.OperationClauseContext):
        pass


    # Enter a parse tree produced by CMLParser#throwsClause.
    def enterThrowsClause(self, ctx:CMLParser.ThrowsClauseContext):
        pass

    # Exit a parse tree produced by CMLParser#throwsClause.
    def exitThrowsClause(self, ctx:CMLParser.ThrowsClauseContext):
        pass


    # Enter a parse tree produced by CMLParser#operationOption.
    def enterOperationOption(self, ctx:CMLParser.OperationOptionContext):
        pass

    # Exit a parse tree produced by CMLParser#operationOption.
    def exitOperationOption(self, ctx:CMLParser.OperationOptionContext):
        pass


    # Enter a parse tree produced by CMLParser#httpMethod.
    def enterHttpMethod(self, ctx:CMLParser.HttpMethodContext):
        pass

    # Exit a parse tree produced by CMLParser#httpMethod.
    def exitHttpMethod(self, ctx:CMLParser.HttpMethodContext):
        pass


    # Enter a parse tree produced by CMLParser#operationTail.
    def enterOperationTail(self, ctx:CMLParser.OperationTailContext):
        pass

    # Exit a parse tree produced by CMLParser#operationTail.
    def exitOperationTail(self, ctx:CMLParser.OperationTailContext):
        pass


    # Enter a parse tree produced by CMLParser#eventTypeRef.
    def enterEventTypeRef(self, ctx:CMLParser.EventTypeRefContext):
        pass

    # Exit a parse tree produced by CMLParser#eventTypeRef.
    def exitEventTypeRef(self, ctx:CMLParser.EventTypeRefContext):
        pass


    # Enter a parse tree produced by CMLParser#operationTarget.
    def enterOperationTarget(self, ctx:CMLParser.OperationTargetContext):
        pass

    # Exit a parse tree produced by CMLParser#operationTarget.
    def exitOperationTarget(self, ctx:CMLParser.OperationTargetContext):
        pass


    # Enter a parse tree produced by CMLParser#contentBlock.
    def enterContentBlock(self, ctx:CMLParser.ContentBlockContext):
        pass

    # Exit a parse tree produced by CMLParser#contentBlock.
    def exitContentBlock(self, ctx:CMLParser.ContentBlockContext):
        pass


    # Enter a parse tree produced by CMLParser#contentEntry.
    def enterContentEntry(self, ctx:CMLParser.ContentEntryContext):
        pass

    # Exit a parse tree produced by CMLParser#contentEntry.
    def exitContentEntry(self, ctx:CMLParser.ContentEntryContext):
        pass


    # Enter a parse tree produced by CMLParser#subdomainAttribute.
    def enterSubdomainAttribute(self, ctx:CMLParser.SubdomainAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#subdomainAttribute.
    def exitSubdomainAttribute(self, ctx:CMLParser.SubdomainAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#contentItem.
    def enterContentItem(self, ctx:CMLParser.ContentItemContext):
        pass

    # Exit a parse tree produced by CMLParser#contentItem.
    def exitContentItem(self, ctx:CMLParser.ContentItemContext):
        pass


    # Enter a parse tree produced by CMLParser#ownerDecl.
    def enterOwnerDecl(self, ctx:CMLParser.OwnerDeclContext):
        pass

    # Exit a parse tree produced by CMLParser#ownerDecl.
    def exitOwnerDecl(self, ctx:CMLParser.OwnerDeclContext):
        pass


    # Enter a parse tree produced by CMLParser#aggregateAttribute.
    def enterAggregateAttribute(self, ctx:CMLParser.AggregateAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#aggregateAttribute.
    def exitAggregateAttribute(self, ctx:CMLParser.AggregateAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#volatility.
    def enterVolatility(self, ctx:CMLParser.VolatilityContext):
        pass

    # Exit a parse tree produced by CMLParser#volatility.
    def exitVolatility(self, ctx:CMLParser.VolatilityContext):
        pass


    # Enter a parse tree produced by CMLParser#criticality.
    def enterCriticality(self, ctx:CMLParser.CriticalityContext):
        pass

    # Exit a parse tree produced by CMLParser#criticality.
    def exitCriticality(self, ctx:CMLParser.CriticalityContext):
        pass


    # Enter a parse tree produced by CMLParser#similarity.
    def enterSimilarity(self, ctx:CMLParser.SimilarityContext):
        pass

    # Exit a parse tree produced by CMLParser#similarity.
    def exitSimilarity(self, ctx:CMLParser.SimilarityContext):
        pass


    # Enter a parse tree produced by CMLParser#setting.
    def enterSetting(self, ctx:CMLParser.SettingContext):
        pass

    # Exit a parse tree produced by CMLParser#setting.
    def exitSetting(self, ctx:CMLParser.SettingContext):
        pass


    # Enter a parse tree produced by CMLParser#moduleAttribute.
    def enterModuleAttribute(self, ctx:CMLParser.ModuleAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#moduleAttribute.
    def exitModuleAttribute(self, ctx:CMLParser.ModuleAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#parameter.
    def enterParameter(self, ctx:CMLParser.ParameterContext):
        pass

    # Exit a parse tree produced by CMLParser#parameter.
    def exitParameter(self, ctx:CMLParser.ParameterContext):
        pass


    # Enter a parse tree produced by CMLParser#parameterList.
    def enterParameterList(self, ctx:CMLParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CMLParser#parameterList.
    def exitParameterList(self, ctx:CMLParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CMLParser#type.
    def enterType(self, ctx:CMLParser.TypeContext):
        pass

    # Exit a parse tree produced by CMLParser#type.
    def exitType(self, ctx:CMLParser.TypeContext):
        pass


    # Enter a parse tree produced by CMLParser#collectionType.
    def enterCollectionType(self, ctx:CMLParser.CollectionTypeContext):
        pass

    # Exit a parse tree produced by CMLParser#collectionType.
    def exitCollectionType(self, ctx:CMLParser.CollectionTypeContext):
        pass


    # Enter a parse tree produced by CMLParser#service.
    def enterService(self, ctx:CMLParser.ServiceContext):
        pass

    # Exit a parse tree produced by CMLParser#service.
    def exitService(self, ctx:CMLParser.ServiceContext):
        pass


    # Enter a parse tree produced by CMLParser#serviceBody.
    def enterServiceBody(self, ctx:CMLParser.ServiceBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#serviceBody.
    def exitServiceBody(self, ctx:CMLParser.ServiceBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#serviceBodyElement.
    def enterServiceBodyElement(self, ctx:CMLParser.ServiceBodyElementContext):
        pass

    # Exit a parse tree produced by CMLParser#serviceBodyElement.
    def exitServiceBodyElement(self, ctx:CMLParser.ServiceBodyElementContext):
        pass


    # Enter a parse tree produced by CMLParser#resource.
    def enterResource(self, ctx:CMLParser.ResourceContext):
        pass

    # Exit a parse tree produced by CMLParser#resource.
    def exitResource(self, ctx:CMLParser.ResourceContext):
        pass


    # Enter a parse tree produced by CMLParser#resourceBody.
    def enterResourceBody(self, ctx:CMLParser.ResourceBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#resourceBody.
    def exitResourceBody(self, ctx:CMLParser.ResourceBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#resourceBodyElement.
    def enterResourceBodyElement(self, ctx:CMLParser.ResourceBodyElementContext):
        pass

    # Exit a parse tree produced by CMLParser#resourceBodyElement.
    def exitResourceBodyElement(self, ctx:CMLParser.ResourceBodyElementContext):
        pass


    # Enter a parse tree produced by CMLParser#consumer.
    def enterConsumer(self, ctx:CMLParser.ConsumerContext):
        pass

    # Exit a parse tree produced by CMLParser#consumer.
    def exitConsumer(self, ctx:CMLParser.ConsumerContext):
        pass


    # Enter a parse tree produced by CMLParser#consumerBody.
    def enterConsumerBody(self, ctx:CMLParser.ConsumerBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#consumerBody.
    def exitConsumerBody(self, ctx:CMLParser.ConsumerBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#consumerBodyElement.
    def enterConsumerBodyElement(self, ctx:CMLParser.ConsumerBodyElementContext):
        pass

    # Exit a parse tree produced by CMLParser#consumerBodyElement.
    def exitConsumerBodyElement(self, ctx:CMLParser.ConsumerBodyElementContext):
        pass


    # Enter a parse tree produced by CMLParser#repository.
    def enterRepository(self, ctx:CMLParser.RepositoryContext):
        pass

    # Exit a parse tree produced by CMLParser#repository.
    def exitRepository(self, ctx:CMLParser.RepositoryContext):
        pass


    # Enter a parse tree produced by CMLParser#repositoryBody.
    def enterRepositoryBody(self, ctx:CMLParser.RepositoryBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#repositoryBody.
    def exitRepositoryBody(self, ctx:CMLParser.RepositoryBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#repositoryBodyElement.
    def enterRepositoryBodyElement(self, ctx:CMLParser.RepositoryBodyElementContext):
        pass

    # Exit a parse tree produced by CMLParser#repositoryBodyElement.
    def exitRepositoryBodyElement(self, ctx:CMLParser.RepositoryBodyElementContext):
        pass


    # Enter a parse tree produced by CMLParser#repositoryMethod.
    def enterRepositoryMethod(self, ctx:CMLParser.RepositoryMethodContext):
        pass

    # Exit a parse tree produced by CMLParser#repositoryMethod.
    def exitRepositoryMethod(self, ctx:CMLParser.RepositoryMethodContext):
        pass


    # Enter a parse tree produced by CMLParser#serviceModifier.
    def enterServiceModifier(self, ctx:CMLParser.ServiceModifierContext):
        pass

    # Exit a parse tree produced by CMLParser#serviceModifier.
    def exitServiceModifier(self, ctx:CMLParser.ServiceModifierContext):
        pass


    # Enter a parse tree produced by CMLParser#resourceModifier.
    def enterResourceModifier(self, ctx:CMLParser.ResourceModifierContext):
        pass

    # Exit a parse tree produced by CMLParser#resourceModifier.
    def exitResourceModifier(self, ctx:CMLParser.ResourceModifierContext):
        pass


    # Enter a parse tree produced by CMLParser#consumerModifier.
    def enterConsumerModifier(self, ctx:CMLParser.ConsumerModifierContext):
        pass

    # Exit a parse tree produced by CMLParser#consumerModifier.
    def exitConsumerModifier(self, ctx:CMLParser.ConsumerModifierContext):
        pass


    # Enter a parse tree produced by CMLParser#dependency.
    def enterDependency(self, ctx:CMLParser.DependencyContext):
        pass

    # Exit a parse tree produced by CMLParser#dependency.
    def exitDependency(self, ctx:CMLParser.DependencyContext):
        pass


    # Enter a parse tree produced by CMLParser#repositoryModifier.
    def enterRepositoryModifier(self, ctx:CMLParser.RepositoryModifierContext):
        pass

    # Exit a parse tree produced by CMLParser#repositoryModifier.
    def exitRepositoryModifier(self, ctx:CMLParser.RepositoryModifierContext):
        pass


    # Enter a parse tree produced by CMLParser#repositoryMethodOption.
    def enterRepositoryMethodOption(self, ctx:CMLParser.RepositoryMethodOptionContext):
        pass

    # Exit a parse tree produced by CMLParser#repositoryMethodOption.
    def exitRepositoryMethodOption(self, ctx:CMLParser.RepositoryMethodOptionContext):
        pass


    # Enter a parse tree produced by CMLParser#visibility.
    def enterVisibility(self, ctx:CMLParser.VisibilityContext):
        pass

    # Exit a parse tree produced by CMLParser#visibility.
    def exitVisibility(self, ctx:CMLParser.VisibilityContext):
        pass


    # Enter a parse tree produced by CMLParser#application.
    def enterApplication(self, ctx:CMLParser.ApplicationContext):
        pass

    # Exit a parse tree produced by CMLParser#application.
    def exitApplication(self, ctx:CMLParser.ApplicationContext):
        pass


    # Enter a parse tree produced by CMLParser#applicationElement.
    def enterApplicationElement(self, ctx:CMLParser.ApplicationElementContext):
        pass

    # Exit a parse tree produced by CMLParser#applicationElement.
    def exitApplicationElement(self, ctx:CMLParser.ApplicationElementContext):
        pass


    # Enter a parse tree produced by CMLParser#commandDecl.
    def enterCommandDecl(self, ctx:CMLParser.CommandDeclContext):
        pass

    # Exit a parse tree produced by CMLParser#commandDecl.
    def exitCommandDecl(self, ctx:CMLParser.CommandDeclContext):
        pass


    # Enter a parse tree produced by CMLParser#flow.
    def enterFlow(self, ctx:CMLParser.FlowContext):
        pass

    # Exit a parse tree produced by CMLParser#flow.
    def exitFlow(self, ctx:CMLParser.FlowContext):
        pass


    # Enter a parse tree produced by CMLParser#flowStep.
    def enterFlowStep(self, ctx:CMLParser.FlowStepContext):
        pass

    # Exit a parse tree produced by CMLParser#flowStep.
    def exitFlowStep(self, ctx:CMLParser.FlowStepContext):
        pass


    # Enter a parse tree produced by CMLParser#flowCommandStep.
    def enterFlowCommandStep(self, ctx:CMLParser.FlowCommandStepContext):
        pass

    # Exit a parse tree produced by CMLParser#flowCommandStep.
    def exitFlowCommandStep(self, ctx:CMLParser.FlowCommandStepContext):
        pass


    # Enter a parse tree produced by CMLParser#flowCommandTail.
    def enterFlowCommandTail(self, ctx:CMLParser.FlowCommandTailContext):
        pass

    # Exit a parse tree produced by CMLParser#flowCommandTail.
    def exitFlowCommandTail(self, ctx:CMLParser.FlowCommandTailContext):
        pass


    # Enter a parse tree produced by CMLParser#flowEventStep.
    def enterFlowEventStep(self, ctx:CMLParser.FlowEventStepContext):
        pass

    # Exit a parse tree produced by CMLParser#flowEventStep.
    def exitFlowEventStep(self, ctx:CMLParser.FlowEventStepContext):
        pass


    # Enter a parse tree produced by CMLParser#flowEventTriggerList.
    def enterFlowEventTriggerList(self, ctx:CMLParser.FlowEventTriggerListContext):
        pass

    # Exit a parse tree produced by CMLParser#flowEventTriggerList.
    def exitFlowEventTriggerList(self, ctx:CMLParser.FlowEventTriggerListContext):
        pass


    # Enter a parse tree produced by CMLParser#flowOperationStep.
    def enterFlowOperationStep(self, ctx:CMLParser.FlowOperationStepContext):
        pass

    # Exit a parse tree produced by CMLParser#flowOperationStep.
    def exitFlowOperationStep(self, ctx:CMLParser.FlowOperationStepContext):
        pass


    # Enter a parse tree produced by CMLParser#flowOperationTail.
    def enterFlowOperationTail(self, ctx:CMLParser.FlowOperationTailContext):
        pass

    # Exit a parse tree produced by CMLParser#flowOperationTail.
    def exitFlowOperationTail(self, ctx:CMLParser.FlowOperationTailContext):
        pass


    # Enter a parse tree produced by CMLParser#flowInitiator.
    def enterFlowInitiator(self, ctx:CMLParser.FlowInitiatorContext):
        pass

    # Exit a parse tree produced by CMLParser#flowInitiator.
    def exitFlowInitiator(self, ctx:CMLParser.FlowInitiatorContext):
        pass


    # Enter a parse tree produced by CMLParser#flowDelegate.
    def enterFlowDelegate(self, ctx:CMLParser.FlowDelegateContext):
        pass

    # Exit a parse tree produced by CMLParser#flowDelegate.
    def exitFlowDelegate(self, ctx:CMLParser.FlowDelegateContext):
        pass


    # Enter a parse tree produced by CMLParser#flowInvocationList.
    def enterFlowInvocationList(self, ctx:CMLParser.FlowInvocationListContext):
        pass

    # Exit a parse tree produced by CMLParser#flowInvocationList.
    def exitFlowInvocationList(self, ctx:CMLParser.FlowInvocationListContext):
        pass


    # Enter a parse tree produced by CMLParser#flowInvocationConnector.
    def enterFlowInvocationConnector(self, ctx:CMLParser.FlowInvocationConnectorContext):
        pass

    # Exit a parse tree produced by CMLParser#flowInvocationConnector.
    def exitFlowInvocationConnector(self, ctx:CMLParser.FlowInvocationConnectorContext):
        pass


    # Enter a parse tree produced by CMLParser#flowInvocation.
    def enterFlowInvocation(self, ctx:CMLParser.FlowInvocationContext):
        pass

    # Exit a parse tree produced by CMLParser#flowInvocation.
    def exitFlowInvocation(self, ctx:CMLParser.FlowInvocationContext):
        pass


    # Enter a parse tree produced by CMLParser#flowInvocationKind.
    def enterFlowInvocationKind(self, ctx:CMLParser.FlowInvocationKindContext):
        pass

    # Exit a parse tree produced by CMLParser#flowInvocationKind.
    def exitFlowInvocationKind(self, ctx:CMLParser.FlowInvocationKindContext):
        pass


    # Enter a parse tree produced by CMLParser#flowEmitsClause.
    def enterFlowEmitsClause(self, ctx:CMLParser.FlowEmitsClauseContext):
        pass

    # Exit a parse tree produced by CMLParser#flowEmitsClause.
    def exitFlowEmitsClause(self, ctx:CMLParser.FlowEmitsClauseContext):
        pass


    # Enter a parse tree produced by CMLParser#flowEventList.
    def enterFlowEventList(self, ctx:CMLParser.FlowEventListContext):
        pass

    # Exit a parse tree produced by CMLParser#flowEventList.
    def exitFlowEventList(self, ctx:CMLParser.FlowEventListContext):
        pass


    # Enter a parse tree produced by CMLParser#coordination.
    def enterCoordination(self, ctx:CMLParser.CoordinationContext):
        pass

    # Exit a parse tree produced by CMLParser#coordination.
    def exitCoordination(self, ctx:CMLParser.CoordinationContext):
        pass


    # Enter a parse tree produced by CMLParser#coordinationStep.
    def enterCoordinationStep(self, ctx:CMLParser.CoordinationStepContext):
        pass

    # Exit a parse tree produced by CMLParser#coordinationStep.
    def exitCoordinationStep(self, ctx:CMLParser.CoordinationStepContext):
        pass


    # Enter a parse tree produced by CMLParser#coordinationPath.
    def enterCoordinationPath(self, ctx:CMLParser.CoordinationPathContext):
        pass

    # Exit a parse tree produced by CMLParser#coordinationPath.
    def exitCoordinationPath(self, ctx:CMLParser.CoordinationPathContext):
        pass


    # Enter a parse tree produced by CMLParser#stateTransition.
    def enterStateTransition(self, ctx:CMLParser.StateTransitionContext):
        pass

    # Exit a parse tree produced by CMLParser#stateTransition.
    def exitStateTransition(self, ctx:CMLParser.StateTransitionContext):
        pass


    # Enter a parse tree produced by CMLParser#targetState.
    def enterTargetState(self, ctx:CMLParser.TargetStateContext):
        pass

    # Exit a parse tree produced by CMLParser#targetState.
    def exitTargetState(self, ctx:CMLParser.TargetStateContext):
        pass


    # Enter a parse tree produced by CMLParser#transitionOperator.
    def enterTransitionOperator(self, ctx:CMLParser.TransitionOperatorContext):
        pass

    # Exit a parse tree produced by CMLParser#transitionOperator.
    def exitTransitionOperator(self, ctx:CMLParser.TransitionOperatorContext):
        pass


    # Enter a parse tree produced by CMLParser#useCase.
    def enterUseCase(self, ctx:CMLParser.UseCaseContext):
        pass

    # Exit a parse tree produced by CMLParser#useCase.
    def exitUseCase(self, ctx:CMLParser.UseCaseContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseBody.
    def enterUseCaseBody(self, ctx:CMLParser.UseCaseBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseBody.
    def exitUseCaseBody(self, ctx:CMLParser.UseCaseBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseActor.
    def enterUseCaseActor(self, ctx:CMLParser.UseCaseActorContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseActor.
    def exitUseCaseActor(self, ctx:CMLParser.UseCaseActorContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseSecondaryActors.
    def enterUseCaseSecondaryActors(self, ctx:CMLParser.UseCaseSecondaryActorsContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseSecondaryActors.
    def exitUseCaseSecondaryActors(self, ctx:CMLParser.UseCaseSecondaryActorsContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseInteractionsBlock.
    def enterUseCaseInteractionsBlock(self, ctx:CMLParser.UseCaseInteractionsBlockContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseInteractionsBlock.
    def exitUseCaseInteractionsBlock(self, ctx:CMLParser.UseCaseInteractionsBlockContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseInteractionItem.
    def enterUseCaseInteractionItem(self, ctx:CMLParser.UseCaseInteractionItemContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseInteractionItem.
    def exitUseCaseInteractionItem(self, ctx:CMLParser.UseCaseInteractionItemContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseInteractionId.
    def enterUseCaseInteractionId(self, ctx:CMLParser.UseCaseInteractionIdContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseInteractionId.
    def exitUseCaseInteractionId(self, ctx:CMLParser.UseCaseInteractionIdContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseReadOperation.
    def enterUseCaseReadOperation(self, ctx:CMLParser.UseCaseReadOperationContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseReadOperation.
    def exitUseCaseReadOperation(self, ctx:CMLParser.UseCaseReadOperationContext):
        pass


    # Enter a parse tree produced by CMLParser#urFeature.
    def enterUrFeature(self, ctx:CMLParser.UrFeatureContext):
        pass

    # Exit a parse tree produced by CMLParser#urFeature.
    def exitUrFeature(self, ctx:CMLParser.UrFeatureContext):
        pass


    # Enter a parse tree produced by CMLParser#urStoryFeature.
    def enterUrStoryFeature(self, ctx:CMLParser.UrStoryFeatureContext):
        pass

    # Exit a parse tree produced by CMLParser#urStoryFeature.
    def exitUrStoryFeature(self, ctx:CMLParser.UrStoryFeatureContext):
        pass


    # Enter a parse tree produced by CMLParser#urNormalFeature.
    def enterUrNormalFeature(self, ctx:CMLParser.UrNormalFeatureContext):
        pass

    # Exit a parse tree produced by CMLParser#urNormalFeature.
    def exitUrNormalFeature(self, ctx:CMLParser.UrNormalFeatureContext):
        pass


    # Enter a parse tree produced by CMLParser#urVerb.
    def enterUrVerb(self, ctx:CMLParser.UrVerbContext):
        pass

    # Exit a parse tree produced by CMLParser#urVerb.
    def exitUrVerb(self, ctx:CMLParser.UrVerbContext):
        pass


    # Enter a parse tree produced by CMLParser#urEntityTail.
    def enterUrEntityTail(self, ctx:CMLParser.UrEntityTailContext):
        pass

    # Exit a parse tree produced by CMLParser#urEntityTail.
    def exitUrEntityTail(self, ctx:CMLParser.UrEntityTailContext):
        pass


    # Enter a parse tree produced by CMLParser#urEntityArticle.
    def enterUrEntityArticle(self, ctx:CMLParser.UrEntityArticleContext):
        pass

    # Exit a parse tree produced by CMLParser#urEntityArticle.
    def exitUrEntityArticle(self, ctx:CMLParser.UrEntityArticleContext):
        pass


    # Enter a parse tree produced by CMLParser#urEntityAttributes.
    def enterUrEntityAttributes(self, ctx:CMLParser.UrEntityAttributesContext):
        pass

    # Exit a parse tree produced by CMLParser#urEntityAttributes.
    def exitUrEntityAttributes(self, ctx:CMLParser.UrEntityAttributesContext):
        pass


    # Enter a parse tree produced by CMLParser#urContainerEntity.
    def enterUrContainerEntity(self, ctx:CMLParser.UrContainerEntityContext):
        pass

    # Exit a parse tree produced by CMLParser#urContainerEntity.
    def exitUrContainerEntity(self, ctx:CMLParser.UrContainerEntityContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseFreeText.
    def enterUseCaseFreeText(self, ctx:CMLParser.UseCaseFreeTextContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseFreeText.
    def exitUseCaseFreeText(self, ctx:CMLParser.UseCaseFreeTextContext):
        pass


    # Enter a parse tree produced by CMLParser#userStory.
    def enterUserStory(self, ctx:CMLParser.UserStoryContext):
        pass

    # Exit a parse tree produced by CMLParser#userStory.
    def exitUserStory(self, ctx:CMLParser.UserStoryContext):
        pass


    # Enter a parse tree produced by CMLParser#userStoryBody.
    def enterUserStoryBody(self, ctx:CMLParser.UserStoryBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#userStoryBody.
    def exitUserStoryBody(self, ctx:CMLParser.UserStoryBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#userStoryXtextBody.
    def enterUserStoryXtextBody(self, ctx:CMLParser.UserStoryXtextBodyContext):
        pass

    # Exit a parse tree produced by CMLParser#userStoryXtextBody.
    def exitUserStoryXtextBody(self, ctx:CMLParser.UserStoryXtextBodyContext):
        pass


    # Enter a parse tree produced by CMLParser#storyValuation.
    def enterStoryValuation(self, ctx:CMLParser.StoryValuationContext):
        pass

    # Exit a parse tree produced by CMLParser#storyValuation.
    def exitStoryValuation(self, ctx:CMLParser.StoryValuationContext):
        pass


    # Enter a parse tree produced by CMLParser#userStoryLine.
    def enterUserStoryLine(self, ctx:CMLParser.UserStoryLineContext):
        pass

    # Exit a parse tree produced by CMLParser#userStoryLine.
    def exitUserStoryLine(self, ctx:CMLParser.UserStoryLineContext):
        pass


    # Enter a parse tree produced by CMLParser#name.
    def enterName(self, ctx:CMLParser.NameContext):
        pass

    # Exit a parse tree produced by CMLParser#name.
    def exitName(self, ctx:CMLParser.NameContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseBenefit.
    def enterUseCaseBenefit(self, ctx:CMLParser.UseCaseBenefitContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseBenefit.
    def exitUseCaseBenefit(self, ctx:CMLParser.UseCaseBenefitContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseScope.
    def enterUseCaseScope(self, ctx:CMLParser.UseCaseScopeContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseScope.
    def exitUseCaseScope(self, ctx:CMLParser.UseCaseScopeContext):
        pass


    # Enter a parse tree produced by CMLParser#useCaseLevel.
    def enterUseCaseLevel(self, ctx:CMLParser.UseCaseLevelContext):
        pass

    # Exit a parse tree produced by CMLParser#useCaseLevel.
    def exitUseCaseLevel(self, ctx:CMLParser.UseCaseLevelContext):
        pass


    # Enter a parse tree produced by CMLParser#stakeholderSection.
    def enterStakeholderSection(self, ctx:CMLParser.StakeholderSectionContext):
        pass

    # Exit a parse tree produced by CMLParser#stakeholderSection.
    def exitStakeholderSection(self, ctx:CMLParser.StakeholderSectionContext):
        pass


    # Enter a parse tree produced by CMLParser#stakeholderItem.
    def enterStakeholderItem(self, ctx:CMLParser.StakeholderItemContext):
        pass

    # Exit a parse tree produced by CMLParser#stakeholderItem.
    def exitStakeholderItem(self, ctx:CMLParser.StakeholderItemContext):
        pass


    # Enter a parse tree produced by CMLParser#stakeholderGroup.
    def enterStakeholderGroup(self, ctx:CMLParser.StakeholderGroupContext):
        pass

    # Exit a parse tree produced by CMLParser#stakeholderGroup.
    def exitStakeholderGroup(self, ctx:CMLParser.StakeholderGroupContext):
        pass


    # Enter a parse tree produced by CMLParser#stakeholder.
    def enterStakeholder(self, ctx:CMLParser.StakeholderContext):
        pass

    # Exit a parse tree produced by CMLParser#stakeholder.
    def exitStakeholder(self, ctx:CMLParser.StakeholderContext):
        pass


    # Enter a parse tree produced by CMLParser#stakeholderAttribute.
    def enterStakeholderAttribute(self, ctx:CMLParser.StakeholderAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#stakeholderAttribute.
    def exitStakeholderAttribute(self, ctx:CMLParser.StakeholderAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#consequences.
    def enterConsequences(self, ctx:CMLParser.ConsequencesContext):
        pass

    # Exit a parse tree produced by CMLParser#consequences.
    def exitConsequences(self, ctx:CMLParser.ConsequencesContext):
        pass


    # Enter a parse tree produced by CMLParser#consequenceItem.
    def enterConsequenceItem(self, ctx:CMLParser.ConsequenceItemContext):
        pass

    # Exit a parse tree produced by CMLParser#consequenceItem.
    def exitConsequenceItem(self, ctx:CMLParser.ConsequenceItemContext):
        pass


    # Enter a parse tree produced by CMLParser#valueRegister.
    def enterValueRegister(self, ctx:CMLParser.ValueRegisterContext):
        pass

    # Exit a parse tree produced by CMLParser#valueRegister.
    def exitValueRegister(self, ctx:CMLParser.ValueRegisterContext):
        pass


    # Enter a parse tree produced by CMLParser#valueCluster.
    def enterValueCluster(self, ctx:CMLParser.ValueClusterContext):
        pass

    # Exit a parse tree produced by CMLParser#valueCluster.
    def exitValueCluster(self, ctx:CMLParser.ValueClusterContext):
        pass


    # Enter a parse tree produced by CMLParser#valueClusterAttribute.
    def enterValueClusterAttribute(self, ctx:CMLParser.ValueClusterAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#valueClusterAttribute.
    def exitValueClusterAttribute(self, ctx:CMLParser.ValueClusterAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#value.
    def enterValue(self, ctx:CMLParser.ValueContext):
        pass

    # Exit a parse tree produced by CMLParser#value.
    def exitValue(self, ctx:CMLParser.ValueContext):
        pass


    # Enter a parse tree produced by CMLParser#valueAttribute.
    def enterValueAttribute(self, ctx:CMLParser.ValueAttributeContext):
        pass

    # Exit a parse tree produced by CMLParser#valueAttribute.
    def exitValueAttribute(self, ctx:CMLParser.ValueAttributeContext):
        pass


    # Enter a parse tree produced by CMLParser#valueElicitation.
    def enterValueElicitation(self, ctx:CMLParser.ValueElicitationContext):
        pass

    # Exit a parse tree produced by CMLParser#valueElicitation.
    def exitValueElicitation(self, ctx:CMLParser.ValueElicitationContext):
        pass


    # Enter a parse tree produced by CMLParser#valueElicitationOption.
    def enterValueElicitationOption(self, ctx:CMLParser.ValueElicitationOptionContext):
        pass

    # Exit a parse tree produced by CMLParser#valueElicitationOption.
    def exitValueElicitationOption(self, ctx:CMLParser.ValueElicitationOptionContext):
        pass


    # Enter a parse tree produced by CMLParser#valueConsequenceEntry.
    def enterValueConsequenceEntry(self, ctx:CMLParser.ValueConsequenceEntryContext):
        pass

    # Exit a parse tree produced by CMLParser#valueConsequenceEntry.
    def exitValueConsequenceEntry(self, ctx:CMLParser.ValueConsequenceEntryContext):
        pass


    # Enter a parse tree produced by CMLParser#valueConsequence.
    def enterValueConsequence(self, ctx:CMLParser.ValueConsequenceContext):
        pass

    # Exit a parse tree produced by CMLParser#valueConsequence.
    def exitValueConsequence(self, ctx:CMLParser.ValueConsequenceContext):
        pass


    # Enter a parse tree produced by CMLParser#valueAction.
    def enterValueAction(self, ctx:CMLParser.ValueActionContext):
        pass

    # Exit a parse tree produced by CMLParser#valueAction.
    def exitValueAction(self, ctx:CMLParser.ValueActionContext):
        pass


    # Enter a parse tree produced by CMLParser#valueEpicClause.
    def enterValueEpicClause(self, ctx:CMLParser.ValueEpicClauseContext):
        pass

    # Exit a parse tree produced by CMLParser#valueEpicClause.
    def exitValueEpicClause(self, ctx:CMLParser.ValueEpicClauseContext):
        pass


    # Enter a parse tree produced by CMLParser#valueEpic.
    def enterValueEpic(self, ctx:CMLParser.ValueEpicContext):
        pass

    # Exit a parse tree produced by CMLParser#valueEpic.
    def exitValueEpic(self, ctx:CMLParser.ValueEpicContext):
        pass


    # Enter a parse tree produced by CMLParser#valueNarrative.
    def enterValueNarrative(self, ctx:CMLParser.ValueNarrativeContext):
        pass

    # Exit a parse tree produced by CMLParser#valueNarrative.
    def exitValueNarrative(self, ctx:CMLParser.ValueNarrativeContext):
        pass


    # Enter a parse tree produced by CMLParser#valueWeigthing.
    def enterValueWeigthing(self, ctx:CMLParser.ValueWeigthingContext):
        pass

    # Exit a parse tree produced by CMLParser#valueWeigthing.
    def exitValueWeigthing(self, ctx:CMLParser.ValueWeigthingContext):
        pass


    # Enter a parse tree produced by CMLParser#rawStatement.
    def enterRawStatement(self, ctx:CMLParser.RawStatementContext):
        pass

    # Exit a parse tree produced by CMLParser#rawStatement.
    def exitRawStatement(self, ctx:CMLParser.RawStatementContext):
        pass


    # Enter a parse tree produced by CMLParser#serviceCutterElement.
    def enterServiceCutterElement(self, ctx:CMLParser.ServiceCutterElementContext):
        pass

    # Exit a parse tree produced by CMLParser#serviceCutterElement.
    def exitServiceCutterElement(self, ctx:CMLParser.ServiceCutterElementContext):
        pass


    # Enter a parse tree produced by CMLParser#scAggregate.
    def enterScAggregate(self, ctx:CMLParser.ScAggregateContext):
        pass

    # Exit a parse tree produced by CMLParser#scAggregate.
    def exitScAggregate(self, ctx:CMLParser.ScAggregateContext):
        pass


    # Enter a parse tree produced by CMLParser#scEntity.
    def enterScEntity(self, ctx:CMLParser.ScEntityContext):
        pass

    # Exit a parse tree produced by CMLParser#scEntity.
    def exitScEntity(self, ctx:CMLParser.ScEntityContext):
        pass


    # Enter a parse tree produced by CMLParser#scSecurityAccessGroup.
    def enterScSecurityAccessGroup(self, ctx:CMLParser.ScSecurityAccessGroupContext):
        pass

    # Exit a parse tree produced by CMLParser#scSecurityAccessGroup.
    def exitScSecurityAccessGroup(self, ctx:CMLParser.ScSecurityAccessGroupContext):
        pass


    # Enter a parse tree produced by CMLParser#scSeparatedSecurityZone.
    def enterScSeparatedSecurityZone(self, ctx:CMLParser.ScSeparatedSecurityZoneContext):
        pass

    # Exit a parse tree produced by CMLParser#scSeparatedSecurityZone.
    def exitScSeparatedSecurityZone(self, ctx:CMLParser.ScSeparatedSecurityZoneContext):
        pass


    # Enter a parse tree produced by CMLParser#scSharedOwnerGroup.
    def enterScSharedOwnerGroup(self, ctx:CMLParser.ScSharedOwnerGroupContext):
        pass

    # Exit a parse tree produced by CMLParser#scSharedOwnerGroup.
    def exitScSharedOwnerGroup(self, ctx:CMLParser.ScSharedOwnerGroupContext):
        pass


    # Enter a parse tree produced by CMLParser#scPredefinedService.
    def enterScPredefinedService(self, ctx:CMLParser.ScPredefinedServiceContext):
        pass

    # Exit a parse tree produced by CMLParser#scPredefinedService.
    def exitScPredefinedService(self, ctx:CMLParser.ScPredefinedServiceContext):
        pass


    # Enter a parse tree produced by CMLParser#scCompatibilities.
    def enterScCompatibilities(self, ctx:CMLParser.ScCompatibilitiesContext):
        pass

    # Exit a parse tree produced by CMLParser#scCompatibilities.
    def exitScCompatibilities(self, ctx:CMLParser.ScCompatibilitiesContext):
        pass


    # Enter a parse tree produced by CMLParser#scUseCase.
    def enterScUseCase(self, ctx:CMLParser.ScUseCaseContext):
        pass

    # Exit a parse tree produced by CMLParser#scUseCase.
    def exitScUseCase(self, ctx:CMLParser.ScUseCaseContext):
        pass


    # Enter a parse tree produced by CMLParser#scUseCaseElement.
    def enterScUseCaseElement(self, ctx:CMLParser.ScUseCaseElementContext):
        pass

    # Exit a parse tree produced by CMLParser#scUseCaseElement.
    def exitScUseCaseElement(self, ctx:CMLParser.ScUseCaseElementContext):
        pass


    # Enter a parse tree produced by CMLParser#scIsLatencyCritical.
    def enterScIsLatencyCritical(self, ctx:CMLParser.ScIsLatencyCriticalContext):
        pass

    # Exit a parse tree produced by CMLParser#scIsLatencyCritical.
    def exitScIsLatencyCritical(self, ctx:CMLParser.ScIsLatencyCriticalContext):
        pass


    # Enter a parse tree produced by CMLParser#scReads.
    def enterScReads(self, ctx:CMLParser.ScReadsContext):
        pass

    # Exit a parse tree produced by CMLParser#scReads.
    def exitScReads(self, ctx:CMLParser.ScReadsContext):
        pass


    # Enter a parse tree produced by CMLParser#scWrites.
    def enterScWrites(self, ctx:CMLParser.ScWritesContext):
        pass

    # Exit a parse tree produced by CMLParser#scWrites.
    def exitScWrites(self, ctx:CMLParser.ScWritesContext):
        pass


    # Enter a parse tree produced by CMLParser#scUseCaseNanoentities.
    def enterScUseCaseNanoentities(self, ctx:CMLParser.ScUseCaseNanoentitiesContext):
        pass

    # Exit a parse tree produced by CMLParser#scUseCaseNanoentities.
    def exitScUseCaseNanoentities(self, ctx:CMLParser.ScUseCaseNanoentitiesContext):
        pass


    # Enter a parse tree produced by CMLParser#scCharacteristic.
    def enterScCharacteristic(self, ctx:CMLParser.ScCharacteristicContext):
        pass

    # Exit a parse tree produced by CMLParser#scCharacteristic.
    def exitScCharacteristic(self, ctx:CMLParser.ScCharacteristicContext):
        pass


    # Enter a parse tree produced by CMLParser#scAvailabilityCriticality.
    def enterScAvailabilityCriticality(self, ctx:CMLParser.ScAvailabilityCriticalityContext):
        pass

    # Exit a parse tree produced by CMLParser#scAvailabilityCriticality.
    def exitScAvailabilityCriticality(self, ctx:CMLParser.ScAvailabilityCriticalityContext):
        pass


    # Enter a parse tree produced by CMLParser#scConsistencyCriticality.
    def enterScConsistencyCriticality(self, ctx:CMLParser.ScConsistencyCriticalityContext):
        pass

    # Exit a parse tree produced by CMLParser#scConsistencyCriticality.
    def exitScConsistencyCriticality(self, ctx:CMLParser.ScConsistencyCriticalityContext):
        pass


    # Enter a parse tree produced by CMLParser#scContentVolatility.
    def enterScContentVolatility(self, ctx:CMLParser.ScContentVolatilityContext):
        pass

    # Exit a parse tree produced by CMLParser#scContentVolatility.
    def exitScContentVolatility(self, ctx:CMLParser.ScContentVolatilityContext):
        pass


    # Enter a parse tree produced by CMLParser#scSecurityCriticality.
    def enterScSecurityCriticality(self, ctx:CMLParser.ScSecurityCriticalityContext):
        pass

    # Exit a parse tree produced by CMLParser#scSecurityCriticality.
    def exitScSecurityCriticality(self, ctx:CMLParser.ScSecurityCriticalityContext):
        pass


    # Enter a parse tree produced by CMLParser#scStorageSimilarity.
    def enterScStorageSimilarity(self, ctx:CMLParser.ScStorageSimilarityContext):
        pass

    # Exit a parse tree produced by CMLParser#scStorageSimilarity.
    def exitScStorageSimilarity(self, ctx:CMLParser.ScStorageSimilarityContext):
        pass


    # Enter a parse tree produced by CMLParser#scStructuralVolatility.
    def enterScStructuralVolatility(self, ctx:CMLParser.ScStructuralVolatilityContext):
        pass

    # Exit a parse tree produced by CMLParser#scStructuralVolatility.
    def exitScStructuralVolatility(self, ctx:CMLParser.ScStructuralVolatilityContext):
        pass


    # Enter a parse tree produced by CMLParser#scNanoentities.
    def enterScNanoentities(self, ctx:CMLParser.ScNanoentitiesContext):
        pass

    # Exit a parse tree produced by CMLParser#scNanoentities.
    def exitScNanoentities(self, ctx:CMLParser.ScNanoentitiesContext):
        pass


    # Enter a parse tree produced by CMLParser#idList.
    def enterIdList(self, ctx:CMLParser.IdListContext):
        pass

    # Exit a parse tree produced by CMLParser#idList.
    def exitIdList(self, ctx:CMLParser.IdListContext):
        pass


    # Enter a parse tree produced by CMLParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:CMLParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by CMLParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:CMLParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by CMLParser#qualifiedName.
    def enterQualifiedName(self, ctx:CMLParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by CMLParser#qualifiedName.
    def exitQualifiedName(self, ctx:CMLParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by CMLParser#channelIdentifier.
    def enterChannelIdentifier(self, ctx:CMLParser.ChannelIdentifierContext):
        pass

    # Exit a parse tree produced by CMLParser#channelIdentifier.
    def exitChannelIdentifier(self, ctx:CMLParser.ChannelIdentifierContext):
        pass



del CMLParser