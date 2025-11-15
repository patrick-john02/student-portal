<script lang="ts">
export const description = "System logs page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbSeparator,
  BreadcrumbLink,
  BreadcrumbPage,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select"

import {
  Table,
  TableRow,
  TableHead,
  TableHeader,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
} from "@/components/ui/dropdown-menu"

import {
  FileDown,
  Trash2,
  MoreHorizontal,
  ServerCrash,
  TerminalSquare,
  AlertTriangle,
  CheckCircle,
} from "lucide-vue-next"

const userRole = "Admin"

const search = ref("")
const severity = ref("all")
const moduleFilter = ref("all")

const logs = ref([
  {
    id: 1,
    message: "User login successful",
    module: "Auth",
    severity: "info",
    icon: CheckCircle,
    timestamp: "2025-01-12 08:22 AM",
  },
  {
    id: 2,
    message: "Failed login attempt",
    module: "Auth",
    severity: "warning",
    icon: AlertTriangle,
    timestamp: "2025-01-12 08:20 AM",
  },
  {
    id: 3,
    message: "Database connection restored",
    module: "System",
    severity: "info",
    icon: TerminalSquare,
    timestamp: "2025-01-11 10:17 PM",
  },
  {
    id: 4,
    message: "API rate limit exceeded",
    module: "API",
    severity: "error",
    icon: ServerCrash,
    timestamp: "2025-01-11 07:15 PM",
  },
])
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>System Logs</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- CONTENT -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Page Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">System Logs</h2>
            <p class="text-sm text-muted-foreground">
              Monitor system errors, warnings, and important activity.
            </p>
          </div>

          <div class="flex gap-2">
            <Button class="flex items-center gap-2">
              <FileDown class="h-4 w-4" />
              Export Logs
            </Button>

            <Button variant="destructive" class="flex items-center gap-2">
              <Trash2 class="h-4 w-4" />
              Clear Logs
            </Button>
          </div>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Log Filters</CardTitle>
            <CardDescription>
              Refine which logs you want to view.
            </CardDescription>
          </CardHeader>

          <CardContent class="flex flex-col md:flex-row gap-4">

            <Input
              v-model="search"
              placeholder="Search logs..."
              class="max-w-xs"
            />

            <Select v-model="moduleFilter">
              <SelectTrigger class="w-[180px]">
                <SelectValue placeholder="Module" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Modules</SelectItem>
                <SelectItem value="Auth">Auth</SelectItem>
                <SelectItem value="API">API</SelectItem>
                <SelectItem value="System">System</SelectItem>
              </SelectContent>
            </Select>

            <Select v-model="severity">
              <SelectTrigger class="w-[180px]">
                <SelectValue placeholder="Severity" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Severities</SelectItem>
                <SelectItem value="info">Info</SelectItem>
                <SelectItem value="warning">Warning</SelectItem>
                <SelectItem value="error">Error</SelectItem>
              </SelectContent>
            </Select>

          </CardContent>
        </Card>

        <!-- LOG TABLE -->
        <Card>
          <CardHeader>
            <CardTitle>System Log Entries</CardTitle>
            <CardDescription>
              View the latest system messages and issues.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Message</TableHead>
                  <TableHead>Module</TableHead>
                  <TableHead>Severity</TableHead>
                  <TableHead>Timestamp</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="log in logs"
                  :key="log.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Message -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <component :is="log.icon" class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ log.message }}</span>
                    </div>
                  </TableCell>

                  <!-- Module -->
                  <TableCell class="text-muted-foreground">
                    {{ log.module }}
                  </TableCell>

                  <!-- Severity -->
                  <TableCell>
                    <Badge
                      :variant="log.severity === 'error' ? 'destructive' : log.severity === 'warning' ? 'secondary' : 'outline'"
                    >
                      {{ log.severity }}
                    </Badge>
                  </TableCell>

                  <!-- Timestamp -->
                  <TableCell class="text-muted-foreground">
                    {{ log.timestamp }}
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Details</DropdownMenuItem>
                        <DropdownMenuItem>Flag Entry</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Log Entry
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
